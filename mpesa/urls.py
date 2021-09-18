"""mpesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from daraja.views import TestView, MakePayment, register_urls, call_back, validation, Confirmation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TestView.as_view()), 
    path('api/v1/lnm/', MakePayment.as_view()),
    path('api/v1/register/', register_urls),
    path('api/v1/callback/', call_back),
    path('api/v1/validation/', validation),
    path('api/v1/confirm/', Confirmation.as_view()),

    path('api/v1/payments/', include("mpesacallbackAPI.api.urls"))
]
