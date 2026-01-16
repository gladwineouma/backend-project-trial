from django.db import models
from trader.models import Trader
from django.utils import timezone

# Create your models here.

class Feedback(models.Model):
    feedback_id = models.CharField(max_length = 10, primary_key=True)
    trader_id = models.ForeignKey(Trader, on_delete=models.CASCADE, default=1)
    feedback_at = models.DateTimeField(default=timezone.now)
    feedback = models.CharField(max_length = 500)

    def __str__(self):
        return f'Feedback {self.feedback_id}'

