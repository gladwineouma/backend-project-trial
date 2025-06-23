from django.db import models
from trader.models import Trader
from product.models import Product
from points.models import Points
class Rewards(models.Model):
    reward_id = models.CharField(max_length=10, primary_key=True, unique=True)
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    recycled_clothes = models.ForeignKey(Product, on_delete=models.CASCADE)
    point = models.ForeignKey(Points, on_delete=models.CASCADE)
    rewards = models.CharField(max_length=100)
    rewards_at = models.DateTimeField()

    def __str__(self):
        return f"{self.reward_id} - {self.rewards}"

