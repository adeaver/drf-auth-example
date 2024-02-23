from django.db import models
from django.contrib.auth.models import User


class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_mask = models.TextField()
    external_service_id = models.TextField()
    external_service_type = models.TextField()
