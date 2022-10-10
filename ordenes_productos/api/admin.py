from django.contrib import admin
from .models import Customer, Customer_Order, Product, Order_Item

admin.site.register(Customer)
admin.site.register(Customer_Order)
admin.site.register(Product)
admin.site.register(Order_Item)
