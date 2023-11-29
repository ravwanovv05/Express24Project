from django.urls import path
from express.api.adminviews import (
    AddCategoryGenericAPIView, AddProductGenericAPIView,
    UserGenericAPIView
)
from express.api.userviews import CategoryGenericAPIView, ProductGenericAPIView, ShoppingCartGenericAPIView

urlpatterns = [
    path('add-category', AddCategoryGenericAPIView.as_view(), name='add_category'),
    path('category', CategoryGenericAPIView.as_view(), name='category'),
    path('add-product', AddProductGenericAPIView.as_view(), name='add_product'),
    path('product/<int:category>', ProductGenericAPIView.as_view(), name='product'),
    path('users', UserGenericAPIView.as_view(), name='users'),
    path('shopping-cart', ShoppingCartGenericAPIView.as_view(), name='shopping_cart'),
]