from django.urls import path
from .views import (
    customers_list_all,
    customer_create_one,
    customer,
    customer_customer_orders_list_all,
    customer_order_create_one,
    customer_order,
    products_list_all,
    product_create_one,
    product,
    order_order_items_list_all,
    order_item_create_one,
    order_item
)

urlpatterns = [
    # ------------------- Restaurants -------------------

    path("customers_list_all/", customers_list_all),
    path("customer_create_one/", customer_create_one),
    path("customer/<int:pk>", customer),

    # ------------------- Customer_Order -------------------

    path("customer_customer_orders_list_all/<int:customer_id>",
         customer_customer_orders_list_all),
    path("customer_order_create_one/<int:customer_id>",
         customer_order_create_one),
    path("customer_order/<int:pk>", customer_order),

    # ------------------- Product -------------------

    path("products_list_all/",
         products_list_all),
    path("product_create_one/",
         product_create_one),
    path("product/<int:pk>", product),

    # ------------------- Order_Item -------------------

    path("order_order_items_list_all/<int:customer_order_id>",
         order_order_items_list_all),
    path("order_item_create_one/<int:customer_order_id>/<int:product_id>",
         order_item_create_one),
    path("order_item/<int:pk>", order_item),
]
