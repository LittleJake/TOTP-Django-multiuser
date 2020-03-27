from django.db import models
import time

# Create your models here.

class totp_user(models.Model):
    secret = models.CharField(max_length=64)
    token = models.CharField(max_length=16)
    ip = models.CharField(max_length=150, unique=True)
    update_time = models.IntegerField(default=0)


