from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

from .models import *

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
	return render(request, 'accounts/dashboard.html',context)

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})

def customer(request,customer_id):
	customer = Customer.objects.get(id=customer_id)
	#here _set will be used bcz top-bottom
	total_orders = customer.order_set.all().count()
	orders = customer.order_set.all()
	context = {'customer':customer, 'orders':orders, 'total_orders':total_orders}
	return render(request, 'accounts/customer.html', context)