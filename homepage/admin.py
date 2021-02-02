from django.contrib import admin
from .models import *
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Email', 'PhoneNo')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','date_ordered','complete', 'transaction_id')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order','customer','quantity','price','ordered','status','date_added')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Email', 'PhoneNo')


class ShippingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'store_address', 'date_added')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')


admin.site.register(ContactForm, ContactAdmin)
admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Shipping,ShippingAdmin)