from django.contrib import admin
from payments.models import Payment_Info, Book_Stor
# Register your models here.

#for addmin site -register Model Class and ModelAdmin Class
class Payment_InfoAdmin(admin.ModelAdmin): #Payment_InfoAdmin is just a class name.
    list_display = ('id','pay_id','pay_method','pay_ammount') #all entry- model attribute name.
admin.site.register(Payment_Info, Payment_InfoAdmin)


admin.site.register(Book_Stor)



class Book_StorAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_quntity','book_price','book_owner')