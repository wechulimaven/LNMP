from django.contrib import admin

from .models import MpesaCallBack, MpesaPayment


admin.site.register(MpesaCallBack)
admin.site.register(MpesaPayment)
