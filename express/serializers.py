from rest_framework.serializers import ModelSerializer
from express.models.categories import Category
from express.models.products import Product, Picture
from django.contrib.auth import get_user_model

from users.models.roles import Role

User = get_user_model()


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class PictureSerializer(ModelSerializer):

    class Meta:
        model = Picture
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

