from django.shortcuts import render, redirect


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

from .forms import OrderForm 
from django.forms import inlineformset_factory
def createOrder(request):
	form = OrderForm() # to construct form 
	if request.method == 'POST': 
		form_data = OrderForm(request.POST)
		if form_data.is_valid():
			form_data.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

#create order from customerpage with customer id
#incase of update order, we sent data to the OrderForm model, with orderid
#but now we are calling it from customer
def createOrderFromCustomer(request, customer_id):

	customer = Customer.objects.get(id=customer_id)
	form = OrderForm(initial = {'customer':customer}) # to construct form for customerid pre-filled
	if request.method == 'POST': 
		form_data = OrderForm(request.POST)
		if form_data.is_valid():
			form_data.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, order_pk):

	order_data = Order.objects.get(id=order_pk)

	form = OrderForm(instance=order_data) # to construct form

	if request.method == 'POST': 
		form_data = OrderForm(request.POST,)# without instance it will craeate a new order
		if form_data.is_valid():
			form_data.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, order_pk):

	order_data = Order.objects.get(id=order_pk)	

	if request.method == 'POST': 
		order_data.delete()
		return redirect('/') 

	context = {'obj_name':order_data}
	return render(request, 'accounts/delete.html', context)