from rest_framework.generics import ListCreateAPIView
# from rest_framework.permissions import IsAdminUser

from .serializers import LNMOnlineSerializer
from mpesacallbackAPI.models import LNMOnline


class LNMOnlineAPIView(ListCreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    # permission_classes = [IsAdminUser]
    def create(self, request):
        mpesa_body =request.body.decode('utf-8')
        # print("MPESA BODY", mpesa_body)
        # print('MPESACALLBACK', request.data)

        merchant_request_id =  request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id =  request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code =  request.data['Body']['stkCallback']['ResultCode']
        amount =  request.data['Body']['stkCallback']['CallbackMetadata']['item'][0]['Value']
        mpesa_receipt_number =  request.data['Body']['stkCallback']['CallbackMetadata']['item'][1]['Value']
        transaction_date =  request.data['Body']['stkCallback']['CallbackMetadata']['item'][3]['Value']
        phone_number =  request.data['Body']['stkCallback']['CallbackMetadata']['item'][4]['Value']
        
        print('MPESACALLBACK AMOUNT', amount)
        print('MPESACALLBACK mpesa_receipt_number', mpesa_receipt_number)
        print('MPESACALLBACK phone_number', phone_number)
        print('MPESACALLBACK merchant_request_id', merchant_request_id)
        print('MPESACALLBACK result_code', result_code)
        return mpesa_body
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
        
        
        