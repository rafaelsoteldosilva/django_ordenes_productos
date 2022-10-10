from dataclasses import fields
from rest_framework import serializers
from .models import Customer, Customer_Order, Product, Order_Item


class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        depth = 1


class Customer_Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Order
        fields = "__all__"
        depth = 1


class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1


class Order_Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = "__all__"
        depth = 1
