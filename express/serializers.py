from rest_framework.serializers import ModelSerializer
from express.models.models import Category
from express.models.models import Product, ShoppingCart, CommentToOrder
from users.models import Role
from users.models.user_model import UserRole, User


class AddCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('title',)


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


class UserRoleSerializer(ModelSerializer):

    class Meta:
        model = UserRole
        fields = ('role',)


class AddUserRoleSerializer(ModelSerializer):

    class Meta:
        model = UserRole
        fields = '__all__'


class RoleSerializer(ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    class Meta:
        model = CommentToOrder
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        return CommentToOrder.objects.create(user=user, **validated_data)

