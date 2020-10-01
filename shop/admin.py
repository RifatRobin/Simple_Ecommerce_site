from django.contrib import admin

# Register your models here.
from .models import Product
admin.site.site_header = "eCom"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)


admin.site.register(Product)
