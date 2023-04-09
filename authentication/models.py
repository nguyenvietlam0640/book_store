from django.db import models

# Create your models here.
from datetime import datetime ,date

import django.utils.timezone as timezone
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    password = models.CharField(max_length=1000, blank=False)
    phone = models.CharField(max_length=12,blank=True)
    birthday = models.DateField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    is_activated = models.BooleanField(default=False)
    class Meta:
        ordering = ('email',)

    def __str__(self):
        return self.email
    def get_absolute_url(self):
        return f'profile/{self.id}'
    
    
