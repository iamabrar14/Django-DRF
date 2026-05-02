from django.http import JsonResponse
from django.db.models import Max
from api.serializers import ProductSerializer,OrderSerializer,OrderItemSerializer,ProductInfoSerializer
from api.models import Product,Order,OrderItem
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class ProductListAPIView(generics.ListAPIView):
    queryset=Product.objects.all() #Get all products from database
    serializer_class=ProductSerializer #Use ProductSerializer to serialize the data

class ProductDetailAPIView(generics.RetrieveAPIView): #Retrive when we want to get a single product by its primary key
     queryset=Product.objects.filter(stock__gt=0) #Only retrieve products that are in stock (stock greater than 0)
     serializer_class=ProductSerializer
     lookup_url_kwarg="product_id"  #Use product_id as the URL parameter to look up the product (in urls.py we will use <int:product_id)


class OrderListAPIView(generics.ListAPIView):
    queryset=Order.objects.prefetch_related('items__product')#Use prefetch_related to optimize database queries by fetching related OrderItem and Product data in a single query
    serializer_class=OrderSerializer #Use OrderSerializer to serialize the data

@api_view(['GET'])
def product_info(request):
    products=Product.objects.all()
    serializer=ProductInfoSerializer({ #Serialize the products, count of products and max price in a single response
        'products':products,
        'count':len(products),
        'max_price':products.aggregate(max_price=Max('price'))['max_price']
        })
    return Response(serializer.data)

    
    


    
    