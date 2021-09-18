from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import LNMOnlineSerializer
from mpesacallbackAPI.models import LNMOnline

from datetime import datetime
import pytz



class LNMOnlineAPIView(ListCreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]

    # def create(self, request):

    #     data = request.data

    #     print("RESPONSE DETA", data)

    #     merchant_request_id = data['Body']['stkCallback']['MerchantRequestID']
    #     checkout_request_id = data['Body']['stkCallback']['CheckoutRequestID']
    #     result_code = data['Body']['stkCallback']['ResultCode']
    #     amount = data['Body']['stkCallback']['CallbackMetadata']['item'][0]['Value']
    #     Result_des = data['Body']['stkCallback']['CallbackMetadata']['item'][2]['Value']
    #     mpesa_receipt_number = data['Body']['stkCallback']['CallbackMetadata']['item'][1]['Value']
    #     transaction_date = data['Body']['stkCallback']['CallbackMetadata']['item'][3]['Value']
    #     phone_number = data['Body']['stkCallback']['CallbackMetadata']['item'][4]['Value']

    #     str_date = str(transaction_date)
    #     formated_transaction_date = datetime.strptime(str_date, "%Y%m%d%H%M%S")

    #     print('MPESACALLBACK AMOUNT', amount)
    #     print('MPESACALLBACK mpesa_receipt_number', mpesa_receipt_number)
    #     print('MPESACALLBACK phone_number', phone_number)
    #     print('MPESACALLBACK merchant_request_id', merchant_request_id)
    #     print('MPESACALLBACK result_code', result_code)

    #     save_model = LNMOnline.objects.create(
            # MerchantRequestID=merchant_request_id,
            # CheckoutRequestID=checkout_request_id,
            # ResultCode=result_code,
            # MpesaReceiptNumber=mpesa_receipt_number,
            # PhoneNumber=phone_number,
            # TransactionDate=formated_transaction_date,
            # Amount=amount,
            # ResultDes=Result_des
    #     )

    #     save_model.save()

    #     return data
    def create(self, request):
        print(request.data, "this is request.data")
        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id, "this should be MerchantRequestID")
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0][
            "Value"
        ]
        print(amount, "this should be an amount")
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][1]["Value"]
        print(mpesa_receipt_number, "this should be an mpesa_receipt_number")

        balance = ""
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][3]["Value"]
        print(transaction_date, "this should be an transaction_date")

        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][
            4
        ]["Value"]
        print(phone_number, "this should be an phone_number")

        
        str_transaction_date = str(transaction_date)
        print(str_transaction_date, "this should be an str_transaction_date")

        transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
        print(transaction_datetime, "this should be an transaction_datetime")

        
        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        print(aware_transaction_datetime, "this should be an aware_transaction_datetime")



        our_model = LNMOnline.objects.create(
            CheckoutRequestID=checkout_request_id,
            MerchantRequestID=merchant_request_id,
            Amount=amount,
            ResultCode=result_code,
            ResultDesc=result_description,
            MpesaReceiptNumber=mpesa_receipt_number,
            TransactionDate=aware_transaction_datetime,
            PhoneNumber=phone_number,
        )

        our_model.save()

        

        return Response({"OurResultDesc": "YEEY!!! It worked!"})
#         {'Body':
#     {'stkCallback':
#         {
#              'MerchantRequestID': '20978-12743857-1',
#             'CheckoutRequestID': 'ws_CO_180920211500594867',
#             'ResultCode': 0,
#             'ResultDesc': 'The service request is processed successfully.',
#             'CallbackMetadata':
#                 {
#               'Item':[
#                         {'Name': 'Amount', 'Value': 1.0},
#                         {'Name': 'MpesaReceiptNumber', 'Value': 'PII733HXHJ'},
#                         {'Name': 'Balance'},
#                         {'Name': 'TransactionDate', 'Value': 20210918150127},
#                         {'Name': 'PhoneNumber', 'Value': 254799143482}
#                     ]
#                 }
#             }
#    }
# }
