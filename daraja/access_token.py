import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from django.conf import settings


def generate_access_token():
    # print('ACCCCCCEESSS',settings.ACCESS_TOKEN_URL)
    res = requests.get(settings.ACCESS_TOKEN_URL, auth=HTTPBasicAuth(settings.CONSUMER_KEY, settings.CONSUMER_SECRETE))
    
    json_response = res.json()
    acess_token = json_response['access_token']
    
    return acess_token




# import requests
# ​
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Bearer SqYSiaz6nW0rOUgehtSsh7CKpjA2'
# }
# ​
# payload = {
#     "BusinessShortCode": 174379,
#     "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwOTE3MTIzNDE0",
#     "Timestamp": "20210917123414",
#     "TransactionType": "CustomerPayBillOnline",
#     "Amount": 1,
#     "PartyA": 254708374149,
#     "PartyB": 174379,
#     "PhoneNumber": 254799143482,
#     "CallBackURL": "https://mydomain.com/path",
#     "AccountReference": "CompanyXLTD",
#     "TransactionDesc": "Payment of X" 
#   }
# ​
# response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
# print(response.text.encode('utf8'))