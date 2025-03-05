from rest_framework import serializers
from cartAndCheckout.models import Cart, CartProduct
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(source='cartproduct_set', many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'total', 'products', 'created_at', 'updated_at']
