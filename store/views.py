from django.shortcuts import render
from .models import *
#views and models are in same directory,so .models

# Create your views here.

def store(request):
    products= Product.objects.all()
    context = {'products':products}
    return render(request,'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        #if the customer is authenticated ie logged in,it work normall
        #else the page will create error
        #to avoid this,else part
    else:
        items = []
        order = {'get_cart_total':0,'get_order_items':0}

    context = {'items':items,'order':order}
    return render(request,'store/cart.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
