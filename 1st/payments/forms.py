from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField()
    gmail = forms.CharField()
    ammounts = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
