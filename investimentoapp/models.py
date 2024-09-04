from django.db import models
from django.utils import timezone


class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateTimeField(default=timezone.now)