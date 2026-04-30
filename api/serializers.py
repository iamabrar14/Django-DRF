from rest_framework import serializers
from .models import Product,Order,OrderItem

class ProductSerializer(serializers.ModelSerializer): #Product Serializer for Product Model
    class Meta:
        model=Product
        fields=(
            'id',
            'name',
            'price',
            'stock'
        )
    
    def validate_price(self,value): #Price Field Validation , price must be greater than zero
        if value <=0:
            raise serializers.ValidationError("Price must be greater than zero.")
        
        return value
    
class OrderItemSerializer(serializers.ModelSerializer): #OrderItem Serializer for OrderItem Model
    product_name=serializers.CharField(source='product.name')
    product_price=serializers.DecimalField(source='product.price',max_digits=10,decimal_places=2)
    class Meta:
        model=OrderItem
        fields=(
            'product_name',
            'product_price',
            'quantity',
            'item_subtotal'
            
        )
    
class OrderSerializer(serializers.ModelSerializer): #Order Serializer for Order Model, includes a nested serializer for order items
    items=OrderItemSerializer(many=True, read_only=True)#Nested Serializer to include order items in the order representation
    total_price=serializers.SerializerMethodField(method_name='total') #Custom field to calculate total price of the order
    
    
    def total(self,obj):
        order_items=obj.items.all() #Get all order items for the order
        return sum(order_item.item_subtotal for order_item in order_items) #Calculate total price by summing the subtotals of each order item
        
    class Meta:
        model=Order
        fields=(
            'order_id',
            'created_at',
            'user',
            'status',
            'items',
            'total_price'
        )
        
class ProductInfoSerializer(serializers.Serializer):
    #Get all products, count of products and Max price
    products=ProductSerializer(many=True)
    count=serializers.IntegerField()
    max_price=serializers.FloatField()
        