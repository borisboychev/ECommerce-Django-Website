from rest_framework import serializers

from api.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Product
        # ('id', 'name', 'description', 'price', 'stock', 'image', 'category')
        fields = "__all__"
