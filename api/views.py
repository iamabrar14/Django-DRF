from django.http import JsonResponse
from django.db.models import Max
from api.serializers import ProductSerializer,OrderSerializer,OrderItemSerializer,ProductInfoSerializer
from api.models import Product,Order,OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET']) #API view that accepts GET requests
def product_list(request):
    products=Product.objects.all() #Get all products from database
    serializer=ProductSerializer(products,many=True) #Serialize the products
    return Response(serializer.data) #Return the serialized data as a response

@api_view(['GET']) 
def product_detail(request,pk): #This function accepts a primary key (pk) as a parameter to retrieve a specific product
    product=get_object_or_404(Product,pk=pk)
    serializer=ProductSerializer(product) 
    return Response(serializer.data) 

@api_view(['GET']) 
def order_list(request):
    orders=Order.objects.all() 
    serializer=OrderSerializer(orders,many=True) 
    return Response(serializer.data) 

@api_view(['GET'])
def product_info(request):
    products=Product.objects.all()
    serializer=ProductInfoSerializer({ #Serialize the products, count of products and max price in a single response
        'products':products,
        'count':len(products),
        'max_price':products.aggregate(max_price=Max('price'))['max_price']
        })
    return Response(serializer.data)

    
    


    
    