from django.contrib import admin
from .models import Product, Costumer, Order, Tag
# Register your models here.
admin.site.register(Product)
admin.site.register(Costumer)
admin.site.register(Order)
admin.site.register(Tag)