from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('payment/', views.payment, name= 'payment'),
    path('paymentform/', views.payment_forms, name='payment_forms'),
    path('books/', views.books, name='books'),
]
