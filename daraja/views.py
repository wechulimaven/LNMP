from django.shortcuts import render
import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from .access_token import generate_access_token

from .utils import formatDateTime
from .encode_base64 import generate_password

from django.conf import settings

import json

from .models import MpesaCallBack

# Create your views here.
class TestView(APIView):
    def get(self, request, format=None):

        access_token = generate_access_token()

        formate_time = formatDateTime()
        decoded_password = generate_password(formate_time)
        return Response({"access_token": access_token, "password": decoded_password})

class MakePayment(APIView):
    def post(self, request, *args, **kwargs):
        requestData = request.data
        amount = requestData["amount"]
        phone = requestData["phone_number"]

        paymentResponse = self.make_mpesa_payment_request(amount=amount, phone=phone)

        return Response(paymentResponse)

    def make_mpesa_payment_request(self, amount: str, phone: str) -> dict:
        access_token = generate_access_token()
        print("ACCESS YOKEN", access_token)
        formate_time = formatDateTime()
        print("ACCESS formatDateTime", formate_time)
        decoded_password = generate_password(formate_time)
        print("ACCESS decoded_password", decoded_password)
        headers = {
                "Authorization": "Bearer %s" % access_token
                }

        print("ACCESS headers", headers)
        payload = {
                    "BusinessShortCode": 174379,
                    "Password": decoded_password,
                    # 'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwOTE3MTgzNzI4',
                            
                    # "Timestamp": "20210917163942",
                    "Timestamp": formate_time,
                    "TransactionType": settings.TRANSACTION_TYPE,
                    "Amount": amount,
                    "PartyA": phone,
                    
                    "PartyB": settings.BUSNESS_SHORT_CODE,
                    "PhoneNumber": phone,
                    "CallBackURL": "https://mydomain.com/path",
                    "AccountReference": settings.ACCOUNT_REFERENCE,
                    "TransactionDesc": settings.TRANSACTION_DESCRIPTION 

                }
        print("ACCESS payload", payload)
        response = requests.post(settings.API_RESOURCE_URL, headers = headers, json = payload)

        string_response = response.text
        string_object = json.loads(string_response)

        print("MPSEA RESPONSE", string_object)

        if 'errorCode' in string_object:
            print('ERROR', string_object['errorMessage'])
            pass
            # return Response(string_object['errorMessage'])

        else:
            merchant_request_id=  string_object["MerchantRequestID"]
            checkout_request_id =  string_object["CheckoutRequestID"]
            response_code =  string_object["ResponseCode"]
            response_description =  string_object["ResponseDescription"]
            customer_message =  string_object["CustomerMessage"]

            data = {
                "MerchantRequestID": merchant_request_id,
                "CheckoutRequestID": checkout_request_id,
                "ResponseCode": response_code,
                "ResponseDescription": response_description,
                "CustomerMessage": customer_message,
            }
            

            save = MpesaCallBack.objects.create(
                merchant_request_id = merchant_request_id,
                checkout_request_id = checkout_request_id,
                response_code = response_code,
                response_description = response_description,
            )
            

            return data

# {
# "amount":"1",
# "phone_number":"254799143482"
# }