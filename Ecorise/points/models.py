from django.db import models
from trader.models import Trader
from pickup_confirmation.models import Confirmation

# Create your models here.

class Points(models.Model):
    points_id = models.CharField(max_length = 10, primary_key = True)
    trader_id = models.ForeignKey(Trader, on_delete = models.CASCADE)
    confirmation_id = models.ForeignKey(Confirmation,on_delete = models.CASCADE)
    points = models.IntegerField()
    points_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Points {self.points_id}'
