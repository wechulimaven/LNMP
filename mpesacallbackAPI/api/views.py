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
        print("MPESA BODY", mpesa_body)
        # print('MPESACALLBACK', request.data)
        
        
        return request.data