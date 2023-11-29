from rest_framework.serializers import ModelSerializer
from express.models.categories import Category
from express.models.products import Product, ShoppingCart
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


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class ShoppingCartSerializer(ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        return ShoppingCart.objects.create(user=user, **validated_data)
