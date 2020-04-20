from django.db import models

# Create your models here.

class Customer(models.Model):
	#null = true helps to import data if any data is empty
	name = models.CharField(max_length = 200, null=True)
	phone = models.CharField(max_length = 200, null=True)
	email = models.CharField(max_length = 200, null=True)
	date_created = models.DateTimeField(auto_now_add = True, null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	#null = db value can be null,true helps to import data if any data is empty
	name = models.CharField(max_length = 200, null=True)
	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = [('Indoor', 'Indoor'),
		('Out Door', 'Out Door'),
	]

	name = models.CharField(max_length = 200, null = True)
	price = models.FloatField(max_length = 200, null = True)
	category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
	#null = db value can be null,true helps to import data if any data is empty
	#blak = form value can be null,true helps to submit data if any field is empty
	description = models.CharField(max_length = 200, null = True, blank=True)
	date_created = models.DateTimeField(auto_now_add = True, null=True)
	#need to make it multi select checkbox
	tags = models.ManyToManyField(Tag, null = True, blank=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = [('Pending', 'Press'),
		('Out for delivery', 'Out for delivery'),
		('Delivered', 'Delivered'),
	]
	# if we delete customer, we want the order to be existed in the DB with a null value
	customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
	#product = models.ManyToManyField(Product, null = True, on_delete = models.SET_NULL)
	product = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add = True, null=True)
	status = models.CharField(max_length = 200, null = True, choices = STATUS)

	def __str__(self):
		return self.product.name
