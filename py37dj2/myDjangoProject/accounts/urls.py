
from django.urls import path
from . import views

urlpatterns = [
  	# name attribute is used to call url link inside href in django way, we can change the path n wont affect that page
    path('register/', views.register, name = "register_page"),
    path('login/', views.log_in, name = "login_page"),
    path('logout/', views.logoutUser, name = "logout_page"),
    path('', views.home, name='home'),
    path('user/', views.userPage, name="user_page"),
    path('products/', views.products, name = 'product_page'),
    path('customer/<str:customer_id>/', views.customer, name='customer_page'),
    path('create_order/', views.createOrder, name= 'create_order_page'),
    path('update_order/<str:order_pk>', views.updateOrder, name= 'update_order_page'),
    path('delete_order/<str:order_pk>', views.deleteOrder, name= 'delete_order_page'),
    path('create_order/<customer_id>', views.createOrderFromCustomer, name= 'create_order_page'),
]