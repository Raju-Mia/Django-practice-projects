from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from payments.models import Payment_Info, Book_Stor
from payments.forms import PaymentForm, BookForm

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
            return HttpResponseRedirect('/home') #home is app urls(if: /main-urls/app-urls) and must give / before the urls.

    else:
        forms = PaymentForm()
        print("get method work")

    #ordinary form fields custom by views username
    forms.order_fields(field_order=['ammounts','gmail','name','password'])

    context = {'form':forms}
    return render(request, 'payments/paymentform.html',context )



def books(request):
    if request.method == 'POST':
        forms = BookForm(request.POST)
        if forms.is_valid():
            print('post method working') #just a print method
        

            name = forms.cleaned_data['book_name'] #book_name is a forms and models fields name
            quntity = forms.cleaned_data['book_quntity'] #book_quntity is a forms and models fields name
            price = forms.cleaned_data['book_price']
            owner = forms.cleaned_data['book_owner']

            #Book_Stor is model name //// book_name, book_quntity are so all fields name are model and forms fields name same.
            p = Book_Stor(book_name=name, book_quntity=quntity, book_price=price, book_owner=owner)
            p.save()

            print("database data save done")

            return HttpResponseRedirect('/home')

    else:
        forms = BookForm()

    context = {'forms':forms}
    return render(request, 'payments/books.html',context )