from django.contrib import admin
from api.models import Order,OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline): #it will show the order item in the order admin page
    model=OrderItem
    
class OrderAdmin(admin.ModelAdmin): #it will show the order item in the order admin page
    inlines=[OrderItemInline]
    
admin.site.register(Order,OrderAdmin)