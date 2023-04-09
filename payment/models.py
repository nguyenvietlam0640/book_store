from django.db import models

# Create your models here.


class Order_session_expired(models.Model):
    token = models.TextField(blank=False)
    status = models.CharField(max_length=7, default='success')
