from django.shortcuts import render,get_object_or_404
from .models import Customers
from django.http import HttpResponse
from django.utils import timezone
from random import randint
from . import date
# Create your views here.
def index(request):
    customers = Customers
    context={
    'list' : customers,
    }
    return render(request,'customers/index.html',context=context)
def add(request):
    list = Customers
    context={
    'list' : list
    }
    return render(request,'customers/add.html',context=context)
def accept(request):
    customer_list = Customers
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
        all = customer_list.objects.order_by('-service_date')[:15]

        context={
            'all' : all,
            'customer' : c,
            'real_date' : real_date
        }
        return render(request,'customers/accept.html',context)
def detail(request,id):
    list = Customers
    print(id)
    c = list.objects.get(pk=id)
    context={
    'customer' : c
    }
    return render (request,'customers/detail.html',context)

def edit(request):
    customer_list = Customers
    try:
        search = request.POST['search']
    except:
        raise
    else:
        if (customer_list.objects.filter(customer_name__startswith = search)):
            c = customer_list.objects.filter(customer_name__startswith = search)
            context={
            'list' : c
            }
            return render(request,'customers/edit.html',context)
        elif (customer_list.objects.filter(customer_lastname__startswith = search)):
            c =customer_list.objects.filter(customer_lastname__startswith = search)
            context={
            'list' : c
            }
            return render(request,'customers/edit.html',context)
        elif (customer_list.objects.filter(customer_id__startswith = search)):
            c = customer_list.objects.filter(customer_id__startswith = search)
            context={
            'list' : c
            }
            return render(request,'customers/edit.html',context)
        elif (customer_list.objects.filter(phone_number__startswith = search)):
            c = customer_list.objects.filter(phone_number__startswith = search)
            context={
            'list' : c
            }
            return render(request,'customers/edit.html',context)
def delete(request,id):
    customer_list = Customers
    c = customer_list.objects.get(pk=id)
    c.delete()
    return HttpResponse('object is deleted')
def update(request,id):
    customer_list = Customers
    c = customer_list.objects.get(pk=id)
    try:
        description = request.POST['description']
        name = request.POST['name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
    except:
        raise
    else:
        c.description = description
        c.save()
        c.customer_name = name
        c.save()
        c.customer_lastname = last_name
        c.save()
        c.phone_number = phone_number
        c.save()
    return HttpResponse('object is updated')
