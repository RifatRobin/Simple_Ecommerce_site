from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Order
admin.site.site_header = "eCom"

# we can also register the model classes in this way given below with @admin.register()
# @admin.register(Product,Contact,Order)

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order id', 'pid')
    # list_filter = ('created',)
