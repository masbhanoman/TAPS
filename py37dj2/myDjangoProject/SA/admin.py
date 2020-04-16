from django.contrib import admin

# Register your models here.
from .models import SA, SA_Item, Finish, CustomerGroup, Customer, Buyer, Salesman

class SAAdmin(admin.ModelAdmin):
    model = SA
admin.site.register(Buyer)
admin.site.register(Salesman)
admin.site.register(Customer)
admin.site.register(CustomerGroup)
admin.site.register(Finish)
admin.site.register(SA_Item)
admin.site.register(SA)