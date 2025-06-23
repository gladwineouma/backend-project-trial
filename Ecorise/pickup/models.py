from django.db import models
from material_pricing.models import Material
from trader.models import Trader

# Create your models here.
class Request(models.Model):
    request_id = models.CharField(max_length = 10, primary_key = True)
    material= models.ForeignKey(Material,to_field = 'material_id', unique = True, on_delete = models.CASCADE)
    trader_id = models.ForeignKey(Trader, to_field = 'trader_id', unique = True, on_delete= models.CASCADE)
    name = models.CharField(max_length = 50)
    phone_number = models.IntegerField(unique = True)
    Created_at = models.DateTimeField(auto_now_add = True)
    location = models.CharField(max_length = 50)
    material_description= models.CharField(max_length = 100)


    def __str__(self):
        return f"Request {self.request_id} by {self.name}"