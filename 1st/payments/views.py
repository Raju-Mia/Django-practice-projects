from django.shortcuts import render
from django.http import HttpResponse

from payments.models import Payment_Info

# Create your views here.
def home(request):
    return render(request, 'payments/home.html')


def payment(request):
    pay_details = Payment_Info.objects.all()
    context = {'details': pay_details}
    return render (request, 'payments/payment.html', context)