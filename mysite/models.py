from django.db import models

# Create your models here.

class totp_user(models.Model):
    appkey = models.CharField(max_length=32, db_index=True)
    token = models.CharField(max_length=16)
    user_id = models.IntegerField(default=0)

