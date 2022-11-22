from django import forms

from .models import Book_Stor

class PaymentForm(forms.Form):
    name = forms.CharField()
    gmail = forms.CharField()
    ammounts = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=4, max_length=12)


class BookForm(forms.Form):
    book_name = forms.CharField()
    book_quntity = forms.IntegerField()
    book_price = forms.IntegerField()
    book_owner = forms.CharField()

    class Meta:

        model = Book_Stor

        exclude = ("user", )