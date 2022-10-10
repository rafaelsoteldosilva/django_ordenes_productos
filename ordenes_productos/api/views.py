from ast import Try
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Customer, Customer_Order, Product, Order_Item
from .serializer import (
    Customer_Serializer,
    Customer_Order_Serializer,
    Product_Serializer,
    Order_Item_Serializer,
)

# ---------------------------- Customer ---------------------------------------------------


@api_view(["GET"])
def customers_list_all(request):
    customers = Customer.objects.all()
    serializer = Customer_Serializer(customers, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def customer_create_one(request):
    my_customer = Customer(
        name_cust=request.data["name_cust"],
        email_cust=request.data["email_cust"],
        phone_cust=request.data["phone_cust"],
        address_cust=request.data["address_cust"],
    )
    my_customer.save()
    return JsonResponse(
        f"The Customer {my_customer.name_cust} was created successfully with id = {my_customer.id}",
        status=status.HTTP_201_CREATED,
        safe=False,
    )


@api_view(["GET", "PUT", "DELETE"])
def customer(request, pk):
    try:
        my_customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(
            {"error": f"The Customer with id '{pk}' doesn't exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = Customer_Serializer(my_customer)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = Customer_Serializer(my_customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        my_customer.delete()
        return Response(f"The Customer '{my_customer.name_cust}', with id = {pk}, was deleted successfully", status=status.HTTP_204_NO_CONTENT)


# --------------------------- Customer_Order ---------------------------------------------------


@api_view(["GET"])
def customer_customer_orders_list_all(request, customer_id):
    customer_orders = Customer_Order.objects.filter(
        customer_cust_ord=customer_id)
    serializer = Customer_Order_Serializer(customer_orders, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def customer_order_create_one(request, customer_id):
    try:
        my_customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(
            {"error": f"The Customer with id '{customer_id}' doesn't exist"}, status=status.HTTP_404_NOT_FOUND
        )
    my_new_customer_order = Customer_Order(
        description_cust_ord=request.data["description_cust_ord"],
        status_cust_ord=request.data["status_cust_ord"],
        customer_cust_ord=my_customer,
    )
    my_new_customer_order.save()
    return JsonResponse(
        f"The Customer Order '{my_new_customer_order.description_cust_ord}' was created successfully for the customer '{my_customer.name_cust}' and id = {my_new_customer_order.id}",
        status=status.HTTP_201_CREATED,
        safe=False,
    )


@api_view(["GET", "PUT", "DELETE"])
def customer_order(request, pk):
    try:
        my_customer_order = Customer_Order.objects.get(pk=pk)
    except Customer_Order.DoesNotExist:
        return Response(
            {"error": f"The Customer Order with id = '{pk}' doesn't exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serializer = Customer_Order_Serializer(my_customer_order)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = Customer_Order_Serializer(
            my_customer_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        my_customer_order.delete()
        return Response(f"The Customer Order '{my_customer_order.description_cust_ord}' with id = '{pk}' was deleted successfully", status=status.HTTP_204_NO_CONTENT)


# --------------------------- Product ---------------------------------------------------

@api_view(["GET"])
def products_list_all(request):
    products = Product.objects.all()
    serializer = Product_Serializer(products, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def product_create_one(request):
    my_product = Product(
        name_prod=request.data["name_prod"],
        description_prod=request.data["description_prod"],
        price_prod=request.data["price_prod"],
        quantity_prod=request.data["quantity_prod"],
    )
    my_product.save()
    return JsonResponse(
        f"The Product '{my_product.name_prod}' was created successfully with id = {my_product.id}",
        status=status.HTTP_201_CREATED,
        safe=False,
    )


@api_view(["GET", "PUT", "DELETE"])
def product(request, pk):
    try:
        my_product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {"error": f"The Product with id '{pk}' doesn't exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = Product_Serializer(my_product)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = Product_Serializer(my_product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        my_product.delete()
        return Response(f"The Product '{my_product.name_prod}', with id = {pk}, was deleted successfully", status=status.HTTP_204_NO_CONTENT)

# --------------------------- Order_Item ------------------------------------------


@api_view(["GET"])
def order_order_items_list_all(request, customer_order_id):
    order_order_items = Order_Item.objects.filter(
        order_ord_item=customer_order_id)
    serializer = Order_Item_Serializer(order_order_items, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def order_item_create_one(request, customer_order_id, product_id):
    try:
        my_customer_order = Customer_Order.objects.get(pk=customer_order_id)
    except Customer_Order.DoesNotExist:
        return Response(
            {"error": f"The Customer Order with id '{customer_order_id}' doesn't exist"}, status=status.HTTP_404_NOT_FOUND
        )
    try:
        my_product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(
            {"error": f"The Product with id '{product_id}' doesn't exist"}, status=status.HTTP_404_NOT_FOUND
        )
    my_new_order_item = Order_Item(
        order_ord_item=my_customer_order,
        product_ord_item=my_product,
        price_ord_item=request.data["price_ord_item"],
        quantity_ord_item=request.data["quantity_ord_item"],
    )
    my_new_order_item.save()
    return JsonResponse(
        f"The Order Item for the product '{my_product.name_prod}' was created successfully for the customer order '{my_customer_order.description_cust_ord}' and id = {my_new_order_item.id}",
        status=status.HTTP_201_CREATED,
        safe=False,
    )


@api_view(["GET", "PUT", "DELETE"])
def order_item(request, pk):
    try:
        my_order_item = Order_Item.objects.get(pk=pk)
    except Order_Item.DoesNotExist:
        return Response(
            {"error": f"The order item with id = '{pk}' doesn't exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serializer = Order_Item_Serializer(my_order_item)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = Order_Item_Serializer(
            my_order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        my_order_item.delete()
        return Response(f"The Order Item with id = '{pk}' was deleted successfully", status=status.HTTP_204_NO_CONTENT)
