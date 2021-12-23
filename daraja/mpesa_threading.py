import json
from threading import Timer

from django.conf import settings
import requests

from access_token import generate_access_token
from encode_base64 import generate_password
from utils import formatDateTime


from models import MpesaCallBack

# def hello():
#     print ("hello, world")

# t = Timer(30.0, hello)
# t.start()

def sendPaymentRequest():
    receiver_numbers = [254799143482, 254745320466]
    amount = 1
    cycle = 0
    while cycle <5:
        cycle +=1
        for num in receiver_numbers:
            t = Timer(30.0, make_mpesa_payment_request(amount, num))
            t.start()


def make_mpesa_payment_request(self, amount: str, phone: str) -> dict:
        print("HUUURRRAYYY....EXECUTED")
        access_token = generate_access_token()
        print("ACCESS YOKEN", access_token)
        formate_time = formatDateTime()
        # print("ACCESS formatDateTime", formate_time)
        decoded_password = generate_password(formate_time)
        # print("ACCESS decoded_password", decoded_password)
        headers = {
                "Authorization": "Bearer %s" % access_token
                }

        # print("ACCESS headers", headers)
        payload = {
           

                    "BusinessShortCode": 174379,
                    "Password": decoded_password,
                    # 'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwOTE3MTgzNzI4',
                            
                    # "Timestamp": "20210917163942",
                    "Timestamp": formate_time,
                    "TransactionType": 'CustomerPayBillOnline',
                    "Amount": amount,
                    "PartyA": phone,
                    
                    "PartyB": '174379',
                    "PhoneNumber": phone,
                    "CallBackURL": "https://lipa-online-payments.herokuapp.com/api/v1/payments/lnm/",
                    "AccountReference": 'CompanyXLTD',
                    "TransactionDesc": 'Payment of X' 

                }
        # print("ACCESS payload", payload)
        response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)

        string_response = response.text
        string_object = json.loads(string_response)

        # print("MPSEA RESPONSE", string_object)

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
            

            model_save = MpesaCallBack.objects.create(
                merchant_request_id = merchant_request_id,
                checkout_request_id = checkout_request_id,
                response_code = response_code,
                response_description = response_description,
            )

            model_save.save()
            

            return data