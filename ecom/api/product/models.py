from django.db import models

# Create your models here.
from api.category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    listed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Product: {self.name}'
