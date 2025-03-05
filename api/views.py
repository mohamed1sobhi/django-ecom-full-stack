from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from cartAndCheckout.models import Product, Cart, CartProduct
from .serializers import ProductSerializer, CartSerializer, CartProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        cart_product.quantity += int(quantity)
        cart_product.save()
        cart.total += product.price * int(quantity)
        cart.save()
        return Response(CartSerializer(cart).data)

    @action(detail=True, methods=['post'])
    def remove_product(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        try:
            cart_product = CartProduct.objects.get(cart=cart, product_id=product_id)
        except CartProduct.DoesNotExist:
            return Response({'error': 'Product not in cart'}, status=status.HTTP_404_NOT_FOUND)
        cart.total -= cart_product.product.price * cart_product.quantity
        cart_product.delete()
        cart.save()
        return Response(CartSerializer(cart).data)
