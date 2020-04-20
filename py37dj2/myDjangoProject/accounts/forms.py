from django.forms import ModelForm
from .models import Order

#we can do classbased form too, but modelform is better n easy
class OrderForm(ModelForm): 
	class Meta:
		model = Order
		fields = '__all__' #['customer', 'product']