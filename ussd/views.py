from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView


import requests
from django.conf import settings
import json

from daraja.access_token import generate_access_token
from daraja.encode_base64 import generate_password
from daraja.utils import formatDateTime
from daraja.models import MpesaCallBack

# Create your views here.


class MpesaUSSD(APIView):

    def make_mpesa_payment_request(self, amount: str, phone: str) -> dict:

        formarted_time = formatDateTime()
        decoded_password = generate_password(formarted_time)
        access_token = generate_access_token()
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": settings.BUSINESS_SHORT_CODE,
            "Password": decoded_password,
            "Timestamp": formarted_time,
            "TransactionType": settings.TRANSACTION_TYPE,  # CustomerPayBillOnline
            "Amount": amount,
            "PartyA": phone,
            "PartyB": settings.BUSINESS_SHORT_CODE,
            "PhoneNumber": phone,
            "CallBackURL": settings.CALL_BACK_URL,
            "AccountReference": settings.ACCOUNT_REFERENCE,
            "TransactionDesc": settings.TRANSACTION_DESCRIPTION
        }

        response = requests.post(settings.API_RESOURCE_URL, json=request, headers=headers)

        mystr = response.text
        obbstr = json.loads(mystr)
        
        response_code = obbstr['ResponseCode']
        if (response_code == "0"):

            merchant_request_id = obbstr['MerchantRequestID']
            checkout_request_id = obbstr['CheckoutRequestID']
            response_description = obbstr['ResponseDescription']

         
            mpesaTransaction= MpesaCallBack.objects.create(
                merchant_request_id = merchant_request_id,
                checkout_request_id = checkout_request_id,
                response_code = response_code,
                response_description = response_description,
            )

            mpesaTransaction.save()

            data = {
                "merchant_request_id": merchant_request_id,
                "checkout_request_id": checkout_request_id,
                "response_description": response_description,
                "response_code": response_code,
                "amount": amount,
                "phone_number_used_for_payment": phone,
            }

            return data



    def post(self, request, *args, **kwargs):
        session_id = request.POST.get("sessionId", None)
        serviceCode = request.POST.get("serviceCode", None)
        phoneNumber = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", None)
        amount = []
        menu_text = ''

            #serve menus based on text
        if text == "":
            menu_text = "CON Welcome to Mpesa Billing System \n"
            menu_text += "1.  Enter Phone number\n"


        elif phoneNumber == phoneNumber:
            menu_text = "CON Enter Amount \n"
            
            resText = text.replace('*', ',')
            splitedText = resText.split(",")
            amount +=splitedText
            # print(amoun)
            
        
        if len(amount) == 2:
            print(amount[1])
            print(phoneNumber)
            paymentResponseData = self.make_mpesa_payment_request(amount = amount[1], phone = amount[0])
            

        return HttpResponse(menu_text, content_type="text/plain")

