from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone



#class Priority(models.Model):
	#priority = models.CharField(
        #max_length=2,
        #choices=priority_choice,
        #default=15,
    #)
	

class Customer(models.Model):
	#how to facilitate group
	customer_name = models.CharField(max_length=30, default = "New Customer", null = True, blank = True, unique=True)
	#group_name = its already created by django manytomany relation

	def __str__(self):
		return self.customer_name
	class Meta:
		ordering = ('customer_name',)

class CustomerGroup(models.Model):
	customer_group_name = models.CharField(max_length=30, default="New Customer Group")
	customer_name = models.ManyToManyField('Customer')	

	def __str__(self):
		return self.customer_group_name
	class Meta:
		ordering = ('customer_group_name',)

class Buyer(models.Model):
	buyer_name = models.CharField(max_length=50, default="New Buyer")
	buyer_brand = models.CharField(max_length=50, blank = True, null=True)

	class Meta:
		ordering = ('buyer_name',)
	
class Salesman(models.Model):
	salesman_id = models.CharField(max_length=7,)
	salesman_name = models.CharField(max_length = 15) 
	
class Finish(models.Model):
	finish_category_choice = [
    	('15', 'Silver'),
    	('12', 'Gunmetal'),
    	('10', 'Copper'),
    	('07', 'Tin'),
    	('03', 'Zinc'),
    	('07', 'Dyeing'),
    	('03', 'Paint'),
    ]
	finish_name = models.CharField(max_length=30, default="finish")
	finish_category = models.CharField(max_length=30, default="None", choices =finish_category_choice,  help_text = 'bath name')
	Default_finish_code = models.CharField(max_length=30, null = True, blank = True, help_text = 'tex finish book')

	def __str__(self):
		return self.finish_name

def new_sa_number():
	last_sa_obj = SA.objects.all().order_by('id').last()
	if not last_sa_obj:
		return '200001'
	last_sa = last_sa_obj.sa_number
	last_sa_int = int(last_sa)
	return last_sa_int+1
last_sa_number = new_sa_number


class SA_Item(models.Model):

	#def add_line_no(self):
		#count = SA.SA_Item.objects.count()
		#return new_sa_number + "_" + (count*10)
	
	item_id = models.CharField(max_length=10, default = last_sa_number, null = True, blank = True)
	#sa_search_id =  models.CharField(max_length=10, default = add_line_no, null = True, blank = True)
	#product_name = pass
	#product_shape = pass
	#logo = pass
	#logo_ref = pass
	#logo_type = pass
	#finish = pass
	#finish_category = pass
	#finish_ref = pass
	#b_part = pass

	#c_part = pass
	#d_part = pass
	#size = pass
	#qty = pass
	#rate = pass
	#item_style =
	#mold_required = boolean
	#sa_delivery_date
	#SA_item_status = press, plating, coating, assembly, packing, audit-hold, hold[if plated cant hold or cancel], canceled, FGS, 
	#mold_delivery_date
	def __str__(self):
		return self.item_id


	class Meta:
		ordering = ('item_id',)

class SA(models.Model):
    # SA no.
    #class buyer(models.model)

    priority_choice = [
    	('15', 'Normal'),
    	('12', 'Urgent'),
    	('10', 'Speed'),
    	('07', 'Fire Urgent'),
    	('03', 'Super Fire Urgent'),
    ]
    sa_created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    sa_number = models.CharField(max_length=500, default = new_sa_number, null = True, blank = True,)
    booking_date = models.DateTimeField(default=timezone.now)
    production_del_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=2,choices=priority_choice,default=15,)#charfield with choice attr
    sa_customer = models.ForeignKey('CustomerGroup', on_delete = models.CASCADE, blank=True, null=True)
    buyer = models.ForeignKey('Buyer', on_delete = models.CASCADE)
    salesman = models.ForeignKey('Salesman', on_delete = models.CASCADE)
    style = models.CharField(max_length=100)
    season = models.CharField(max_length=10)
    washing_type = models.CharField(max_length=10)
    b_c_d_part_finish = models.ForeignKey('Finish', on_delete = models.CASCADE)
    wash_ref = models.CharField(max_length=50)
    other_requirements = models.TextField(max_length=50)

    #sa_closing_date = models.DateField(blank=True, null=True)

    sa_item = models.ManyToManyField(SA_Item)

    def __str__(self):
    	return self.sa_number

    class Meta:
    	ordering = ('sa_number',)
