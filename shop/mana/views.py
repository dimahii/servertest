from django.shortcuts import render,get_object_or_404
from .models import Customers
from django.http import HttpResponse
from django.utils import timezone
from random import randint
from . import date
# Create your views here.
def add(request):
    list = Customers
    context={
    'list' : list
    }
    return render(request,'customers/add.html',context=context)
def accept(request):
    list = Customers
    try:
        description = request.POST['description']
        name = request.POST['name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        customer_id = randint(10000,100000)
    except:
        raise
    else:
        c = Customers(customer_name=name,description=description,customer_lastname=last_name,phone_number=phone_number,customer_id=customer_id)
        c.save()
        real_date=date.gregorian_to_jalali(timezone.now().year,timezone.now().month,timezone.now().day)
        context={
            'customer' : c,
            'real_date' : real_date
        }
        return render(request,'customers/accept.html',context)
