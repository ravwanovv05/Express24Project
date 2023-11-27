from django.urls import path
from express.api.adminviews import AddCategoryGenericAPIView, AddProductGenericAPIView, AddPictureGenericAPIView
from express.api.userviews import CategoryGenericAPIView


urlpatterns = [
    path('add-category', AddCategoryGenericAPIView.as_view(), name='add_category'),
    path('category', CategoryGenericAPIView.as_view(), name='category'),
    path('add-product', AddProductGenericAPIView.as_view(), name='add_product'),
    path('add-picture', AddPictureGenericAPIView.as_view(), name='add_picture'),
]