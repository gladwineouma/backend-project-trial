from django.db import models
from material_pricing.models import Material
from trader.models import Trader

# Create your models here.
class Request(models.Model):
    request_id = models.CharField(max_length = 10, primary_key = True)
    material= models.ForeignKey(Material,  on_delete = models.CASCADE, null=True, blank=True)
    trader_id = models.ForeignKey(Trader,on_delete= models.CASCADE)
    name = models.CharField(max_length=(50), null=True, blank=True)
    phone_number = models.IntegerField(unique = True)
    Created_at = models.DateTimeField(auto_now_add = True)
    location = models.CharField(max_length = 50)
    material_description= models.CharField(max_length = 100)


    def __str__(self):
        return f"Request {self.request_id} by {self.name}"