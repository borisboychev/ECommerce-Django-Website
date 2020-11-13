from django.contrib import admin

# Register your models here.
from api.order.models import Order

admin.site.register(Order)