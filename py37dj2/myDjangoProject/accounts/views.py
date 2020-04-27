from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.http import HttpResponse

from .models import * #for data manipulation
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import messages
def register(request):

	if request.user.is_authenticated:
		return redirect('home')
	else:

		#it will handle unique user, passwprd strength, pass hashing..everything
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				#will show flush message, its stored in the template
				messages.success(request, 'Account is created for ' + username)
				return redirect('login_page')

		context = {'form': form}
		return render(request, 'accounts/register.html', context)


from django.contrib.auth import authenticate, login, logout

def log_in(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		curr_user = authenticate(request, username=username, password = password)
		
		if curr_user is not None:
			login(request, curr_user)
			return redirect('home')
		else:
			messages.info(request, "Username or Password is incorrect")

	context = {}
	return render(request, 'accounts/login.html', context)
	
def logoutUser(request):
	logout(request)
	return redirect('login_page')


def userPage(request):
	context = {}
	return render(request, 'accounts/user_page.html', context)


from django.contrib.auth.decorators import login_required


@login_required(login_url='login_page')
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
	return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login_page')
def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})

from .filters import OrderFilter
@login_required(login_url='login_page')
def customer(request,customer_id):
	customer = Customer.objects.get(id=customer_id)
	#here _set will be used bcz top-bottom
	total_orders = customer.order_set.all().count()
	orders = customer.order_set.all()

	my_filter = OrderFilter(request.GET, queryset=orders)
	orders = my_filter.qs

	context = {'customer':customer, 'orders':orders, 'total_orders':total_orders, 'my_filter':my_filter}
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
	context = {'formset':form}
	return render(request, 'accounts/order_form.html', context)

#not working as expected, maybe because one of them has to be manytomany rel
#def createOrder(request):
#	OrderFormSet = inlineformset_factory(Product, Order ,fields=('__all__'), form=OrderForm, can_delete=True)
	#form = OrderForm() # to construct form 
#	formset = OrderFormSet()
#	if request.method == 'POST': 
#		form_data = OrderForm(request.POST)
#		if form_data.is_valid():
#			return redirect('/')
#	context = {'formset':formset}
#	return render(request, 'accounts/order_form.html', context)

#create order from customerpage with customer id
#incase of update order, we sent data to the OrderForm model, with orderid
#but now we are calling it from customer
def createOrderFromCustomer(request, customer_id):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra =10)
	customer = Customer.objects.get(id=customer_id)
	#form = OrderForm(initial = {'customer':customer}) # to construct form for customerid pre-filled
	formset = OrderFormSet(queryset = Order.objects.none(), instance=customer)
	if request.method == 'POST': 
		form_data = OrderFormSet(request.POST, instance=customer)
		if form_data.is_valid():
			form_data.save()
			return redirect('/')
	context = {'formset':formset}
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

