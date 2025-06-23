from django.db import models

from pickup.models import Request
from material_pricing.models import Material
from recyclers.models import Recyclers
from trader.models import Trader


# Create your models here.
class Confirmation(models.Model):
    confirmation_id = models.CharField(max_length = 10, primary_key=True)
    request = models.ForeignKey(Request,to_field = 'request_id',on_delete = models.CASCADE)
    material = models.ForeignKey(Material,to_field = 'material_id',on_delete = models.CASCADE)
    recycler = models.ForeignKey(Recyclers,to_field = 'recycler_id', on_delete = models.CASCADE)
    trader = models.ForeignKey(Trader,to_field = 'trader_id', on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    phone_number = models.IntegerField(unique = True)
    location = models.CharField(max_length = 50)
    confirmed_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Confirmation {self.confirmation_id}'











