from django.contrib import admin

# Register your models here.
from api.category.models import Category

admin.site.register(Category)