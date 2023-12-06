from django.urls import path
from express.api.adminviews import (
    AddCategoryGenericAPIView, AddProductGenericAPIView,
    UserInfoGenericAPIView, ApplicationGenericAPIView, UpdateDestroyUserRoleAPIView, UserRoleGenericAPIView,
    RoleGenericAPIView
)
from express.api.userviews import (
    CategoryGenericAPIView, ProductGenericAPIView, ShoppingCartGenericAPIView,
    UpdateDestroyShoppingCartGenericAPIView, IncrementShoppingCartGenericAPIVIew,
    DecrementShoppingCartGenericAPIVIew, CommentGenericAPIView
)


urlpatterns = [
    path('add-category', AddCategoryGenericAPIView.as_view(), name='add_category'),
    path('category', CategoryGenericAPIView.as_view(), name='category'),
    path('add-product', AddProductGenericAPIView.as_view(), name='add_product'),
    path('product/<int:category>', ProductGenericAPIView.as_view(), name='product'),
    path('user-info', UserInfoGenericAPIView.as_view(), name='user_info'),
    path('add-role', UserRoleGenericAPIView.as_view(), name='add_role'),
    path('roles', RoleGenericAPIView.as_view(), name='roles'),
    path('update-role/<int:user>', UpdateDestroyUserRoleAPIView.as_view(), name='update_role'),
    path('shopping-cart', ShoppingCartGenericAPIView.as_view(), name='shopping_cart'),
    path('delete-cart/<int:pk>', UpdateDestroyShoppingCartGenericAPIView.as_view(), name='delete_cart'),
    path('increment-product/<int:pk>', IncrementShoppingCartGenericAPIVIew.as_view(), name='increment_product'),
    path('decrement-product/<int:pk>', DecrementShoppingCartGenericAPIVIew.as_view(), name='decrement_product'),
    path('application', ApplicationGenericAPIView.as_view(), name='application'),
    path('add-comment', CommentGenericAPIView.as_view(), name='add_comment'),
]

