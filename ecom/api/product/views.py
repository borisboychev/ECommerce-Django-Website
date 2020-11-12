from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.product.models import Product
from api.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
