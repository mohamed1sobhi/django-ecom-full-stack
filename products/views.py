from django.shortcuts import render
from . import models
from .forms import ProductForm, CategoryForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# class bassed view to create a new product  
class ProductCreateView(LoginRequiredMixin,CreateView):
    model = models.Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')


    #class bassed view to update a product
class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')


    #class bassed view to delete a product
class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


    #class bassed view to create a new category 
class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = models.Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')


    #class bassed view to update a category
class CategoryUpdateView(UpdateView):
    model = models.Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')


    #view to retrieve all products
def product_list(request):
    products = models.Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)


    #view to retrieve a single product
def product_detail(request, id):
    product_detail = models.Product.objects.get(id=id)
    context = {
        'product_detail': product_detail
    }
    return render(request, 'product_detail.html', context)


    #view to retrieve all categories
def category_list(request):
    category = models.Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'category_list.html', context)

    #view to retrieve all products in a category
def category_detail(request, id=None):
    if id is not None:
        category_detail = models.Category.objects.get(id=id)
        products = models.Product.objects.filter(category=category_detail)
    else:
        category_detail = None
        products = models.Product.objects.all()

    context = {
        'category_detail': category_detail,
        'products': products,
    }
    return render(request, 'product_list.html', context)


