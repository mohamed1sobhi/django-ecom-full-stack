from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, CartProduct
from products.models import Product

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id) 
    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total': 0}) 
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_product.quantity += 1
        cart_product.save()
    cart.total = sum(item.product.price * item.quantity for item in cart.cartproduct_set.all())
    cart.save()
    return redirect('cart')  


@login_required
def remove_from_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_product = CartProduct.objects.filter(cart=cart, product=product).first()
    if cart_product:
        if cart_product.quantity > 1:
            cart_product.quantity -= 1
            cart_product.save()
        else:
            cart_product.delete()   
        cart.total = sum(item.product.price * item.quantity for item in cart.cartproduct_set.all())
        cart.save()
    return redirect('cart') 



@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)