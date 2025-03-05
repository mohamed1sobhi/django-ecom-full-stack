from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:id>/', views.category_detail, name='category_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
]