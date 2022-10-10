from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
import re

# Create your models here.


class Customer_fields_validators:
    def phone_number(value):
        reg = re.compile(
            "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$")
        if not reg.match(value):
            raise ValidationError(f"{value} is not a valid phone number")

# Customer
# 	name
# 	email
#   phone
# 	address


class Customer(models.Model):
    name_cust = models.CharField(max_length=100)
    email_cust = models.EmailField(max_length=254)
    phone_cust = models.CharField(
        max_length=20,
        validators=[
            Customer_fields_validators.phone_number,
        ],
    )
    address_cust = models.CharField(max_length=500)

    def __str__(self):
        return self.name_cust


# Customer_Order
# 	customer
# 	description
#   status (1 = pending, 2 = in progress, 3 = delivered)


class Customer_Order(models.Model):
    description_cust_ord = models.CharField(max_length=500)
    customer_cust_ord = models.ForeignKey(
        Customer, on_delete=models.CASCADE, default=1
    )
    status_cust_ord = models.IntegerField(default=1)

    def __str__(self):
        return self.description_cust_ord

# Producto
# 	Nombre
# 	Descripción
# 	Precio
# 	Cantidad en Inventario


class Product(models.Model):
    name_prod = models.CharField(max_length=100)
    description_prod = models.CharField(max_length=500)
    price_prod = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_prod = models.IntegerField(default=1)

    def __str__(self):
        return self.name_prod

# Order_Items
# 	Orden id
# 	Producto id
# 	Precio
# 	Cantidad


class Order_Item(models.Model):
    order_ord_item = models.ForeignKey(
        Customer_Order, on_delete=models.CASCADE, default=1
    )
    product_ord_item = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=1
    )
    price_ord_item = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_ord_item = models.IntegerField(default=1)

    def __str__(self):
        return str(self.order_ord_prod) + " - " + str(self.product_ord_prod)
