from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
from api.category.models import Category
from api.category.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
