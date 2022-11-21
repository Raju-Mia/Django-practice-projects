from django.shortcuts import render
from django.http import HttpResponse

from payments.models import Payment_Info
from payments.forms import PaymentForm

# Create your views here.
def home(request):
    return render(request, 'payments/home.html')


def payment(request):
    pay_details = Payment_Info.objects.all()
    context = {'details': pay_details}
    return render (request, 'payments/payment.html', context)


def payment_forms(request):
    if request.method == 'POST':
        forms = PaymentForm(request.POST)
        if forms.is_valid():
            print('POST METHOD WORK')

            """form.cleaned_data returns a dictionary of validated form input fields 
            and their values, where string primary keys are returned as objects."""
            print(forms.cleaned_data)

    else:
        forms = PaymentForm()
        print("get method work")

    #ordinary form fields custom by views username
    forms.order_fields(field_order=['ammounts','gmail','name','password'])

    context = {'form':forms}
    return render(request, 'payments/paymentform.html',context )