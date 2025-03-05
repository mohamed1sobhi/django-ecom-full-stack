from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('carts', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
