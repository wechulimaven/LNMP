from django.db import models
class LNMOnline(models.Model):
    MerchantRequestID = models.CharField(max_length=50,blank=True, null=True)
    CheckoutRequestID = models.CharField(max_length=50,blank=True, null=True)
    ResultCode = models.IntegerField(max_length=50, blank=True, null=True)
    MpesaReceiptNumber = models.CharField(max_length=50,blank=True, null=True)
    PhoneNumber = models.CharField(max_length=13,blank=True, null=True)
    TransactionDate = models.DateField(blank=True, null=True)
    Amount = models.FloatField(max_length=50, blank=True, null=True)
    ResultDes = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        f'{self.MerchantRequestID} - {self.Amount} - {self.MpesaReceiptNumber}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'LNMOnline'
        verbose_name_plural = 'LNMOnlines'