# store/admin.py
from django.contrib import admin
from .models import User, Item, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'quantity', 'order_date')
    list_filter = ('order_date', 'user', 'item')
    date_hierarchy = 'order_date'