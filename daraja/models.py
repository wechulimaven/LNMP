from django.db import models

class MpesaCallBack(models.Model):
    merchant_request_id = models.CharField(max_length=50)
    checkout_request_id = models.CharField(max_length=50)
    response_code = models.CharField(max_length=50)
    response_description = models.CharField(max_length=50)
    customer_message = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.merchant_request_id} - {self.customer_message}'
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'MpesaCallBack'
        verbose_name_plural = 'MpesaCallBacks'
