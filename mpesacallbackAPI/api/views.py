from rest_framework.generics import ListCreateAPIView
# from rest_framework.permissions import IsAdminUser

from .serializers import LNMOnlineSerializer
from mpesacallbackAPI.models import LNMOnline

from datetime import datetime


class LNMOnlineAPIView(ListCreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    # permission_classes = [IsAdminUser]

    def create(self, request):

        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code = request.data['Body']['stkCallback']['ResultCode']
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['item'][0]['Value']
        Result_des = request.data['Body']['stkCallback']['CallbackMetadata']['item'][2]['Value']
        mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['item'][1]['Value']
        transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['item'][3]['Value']
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['item'][4]['Value']

        str_date = str(transaction_date)
        formated_transaction_date = datetime.strptime(str_date, "%Y%m%d%H%M%S")

        print('MPESACALLBACK AMOUNT', amount)
        print('MPESACALLBACK mpesa_receipt_number', mpesa_receipt_number)
        print('MPESACALLBACK phone_number', phone_number)
        print('MPESACALLBACK merchant_request_id', merchant_request_id)
        print('MPESACALLBACK result_code', result_code)

        save_model = LNMOnline.objects.create(
            MerchantRequestID=merchant_request_id,
            CheckoutRequestID=checkout_request_id,
            ResultCode=result_code,
            MpesaReceiptNumber=mpesa_receipt_number,
            PhoneNumber=phone_number,
            TransactionDate=formated_transaction_date,
            Amount=amount,
            ResultDes=Result_des
        )

        save_model.save()

        return save_model
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
