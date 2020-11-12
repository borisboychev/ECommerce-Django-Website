from django.contrib import admin

# Register your models here.
from api.product.models import Product

admin.site.register(Product)
