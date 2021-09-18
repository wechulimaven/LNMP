from django.urls import path
from .views import LNMOnlineAPIView

urlpatterns = [ 
    path('lnm/', LNMOnlineAPIView.as_view()),
    ]
