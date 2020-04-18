
from django.urls import path
from . import views

urlpatterns = [
  	# name attribute is used to call url link inside href in django way, we can change the path n wont affect that page
    path('', views.home, name='home'),
    path('products/', views.products, name = 'product_page'),
    path('customer/<str:customer_id>/', views.customer, name='customer_page'),
]