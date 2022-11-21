from django.contrib import admin
from payments.models import Payment_Info
# Register your models here.

#for addmin site -register Model Class and ModelAdmin Class
class Payment_InfoAdmin(admin.ModelAdmin): #Payment_InfoAdmin is just a class name.
    list_display = ('id','pay_id','pay_method','pay_ammount') #all entry- model attribute name.
admin.site.register(Payment_Info, Payment_InfoAdmin)