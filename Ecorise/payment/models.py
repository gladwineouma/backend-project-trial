from django.db import models
from trader.models import Trader
from recyclers.models import Recyclers
from pickup_confirmation.models import Confirmation
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True, unique=True)
    trader_id = models.ForeignKey(Trader, on_delete=models.CASCADE)
    confirmation_id = models.ForeignKey(Confirmation, on_delete=models.CASCADE)
    recycler_id = models.ForeignKey(Recyclers, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30, default='M-Pesa')
    payment_status = models.CharField(max_length=30, choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed')])
    phone_number = models.IntegerField()
    mpesa_receipt_number = models.CharField(max_length=100)
    paid_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Payment {self.payment_id}'
# Create your models here.



