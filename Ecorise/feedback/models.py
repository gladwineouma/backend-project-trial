from django.db import models
from trader.models import Trader

# Create your models here.

class Feedback(models.Model):
    feedback_id = models.CharField(max_length = 10, primary_key=True)
    trader_id = models.ForeignKey(Trader,to_field = 'trader_id', unique = True, on_delete = models.CASCADE)
    feedback_at = models.DateTimeField(auto_now_add = True)
    feedback = models.CharField(max_length = 500)

    def __str__(self):
        return f'Feedback {self.feedback_id}'

