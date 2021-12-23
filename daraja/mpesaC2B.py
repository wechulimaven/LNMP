import json
from threading import Timer

from django.conf import settings
import requests

from access_token import generate_access_token
from encode_base64 import generate_password
from utils import formatDateTime


from models import MpesaCallBack


def initiateC2Bpayment(amount: str, phoneNumber: str, billNumber: str, commandId: str, ):

    access_token = generate_access_token()
    formate_time = formatDateTime()
    decoded_password = generate_password(formate_time)
    headers = {
        "Authorization": "Bearer %s" % access_token
    }

    payload = {
        "ShortCode": "600996",
        "CommandID": commandId,
        "Amount": amount,
        "Msisdn": phoneNumber,
        "BillRefNumber": billNumber
    }
    # print("ACCESS payload", payload)
    response = requests.post(
        'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate', headers=headers, json=payload)

    string_response = response.text
    string_object = json.loads(string_response)
