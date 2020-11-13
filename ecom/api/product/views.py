from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = uSERobjects.all().order_by('id')
    serializer_class = ProductSerializer
