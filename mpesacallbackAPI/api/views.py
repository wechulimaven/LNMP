from rest_framework.generics import ListCreateAPIView
# from rest_framework.permissions import IsAdminUser

from .serializers import LNMOnlineSerializer
from mpesacallbackAPI.models import LNMOnline


class LNMOnlineAPIView(ListCreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    # permission_classes = [IsAdminUser]
    def create(self, request):
        print('MPESACALLBACK', request.data)
        return request.data