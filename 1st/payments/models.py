from django.db import models

# Create your models here.

class Payment_Info(models.Model):
    pay_id = models.IntegerField()
    pay_method = models.CharField(max_length=25)
    pay_ammount = models.IntegerField()



class Book_Stor(models.Model):
    book_name = models.CharField(max_length=25)
    book_quntity = models.IntegerField()
    book_price = models.IntegerField()
    book_owner = models.CharField(max_length=25)

    def __str__(self):
        return self.book_name
