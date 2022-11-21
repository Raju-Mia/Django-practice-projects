from django.db import models

# Create your models here.

class Payment_Info(models.Model):
    pay_id = models.IntegerField()
    pay_method = models.CharField(max_length=25)
    pay_ammount = models.IntegerField()

    