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

class MpesaPayment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    organization_balance = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name} - {self.amount}- {self.reference}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'MpesaPayment'
        verbose_name_plural = 'MpesaPayments'
