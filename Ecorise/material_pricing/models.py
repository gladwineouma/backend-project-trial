from django.db import models

# Create your models here.

class Material(models.Model):
    material_id = models.AutoField(primary_key = True)
    material_type = models.CharField(max_length = 100)
    price_per_kg = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)

