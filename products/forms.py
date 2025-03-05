from django.forms import ModelForm
from .models import Product,Category



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'rating', 'category', 'thumbnail']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']