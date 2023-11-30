from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from express.models.products import ShoppingCart, Product, CommentToOrder
from users.roles import UserRole
from users.permissions import IsAdminPermission, IsCourierPermissions
from express.serializers import (
    CategorySerializer, ProductSerializer, UserSerializer,
    ShoppingCartSerializer, UserRoleSerializer
)

User = get_user_model()


class AddCategoryGenericAPIView(GenericAPIView):
    permission_classes = (IsAdminPermission, IsAuthenticated)
    serializer_class = CategorySerializer

    def post(self, request):
        serializer_category = self.get_serializer(data=request.data)
        serializer_category.is_valid(raise_exception=True)
        serializer_category.save()
        return Response(serializer_category.data)


class AddProductGenericAPIView(GenericAPIView):
    permission_classes = (IsAdminPermission, IsAuthenticated)
    serializer_class = ProductSerializer

    def post(self, request):
        serializer_product = self.get_serializer(data=request.data)
        serializer_product.is_valid(raise_exception=True)
        serializer_product.save()
        return Response(serializer_product.data)


class UserInfoGenericAPIView(GenericAPIView):
    permission_classes = (IsAdminPermission, IsAuthenticated)
    serializer_class = UserSerializer

    def get_object(self, pk):
        return UserRole.objects.get(Q(user=pk)).role.title

    def get(self, request):
        users = User.objects.all().order_by('-date_joined')
        serializer_user = self.get_serializer(users, many=True)
        list_data = serializer_user.data
        new_list_data = []
        for data in list_data:
            data['role'] = self.get_object(data['id'])
            new_list_data.append(data)

        return Response(new_list_data)


class ApplicationGenericAPIView(GenericAPIView):
    permission_classes = (IsAdminPermission, IsAuthenticated)
    serializer_class = ShoppingCartSerializer or IsCourierPermissions

    def get(self, request):
        shopping_cart = ShoppingCart.objects.all()
        serializer_shopping_cart = self.get_serializer(shopping_cart, many=True)
        list_data = serializer_shopping_cart.data
        new_list_data = []
        for data in list_data:
            first_name = User.objects.get(pk=data['user']).first_name
            last_name = User.objects.get(pk=data['user']).last_name
            data['full_name'] = f"{first_name} {last_name}"
            data['title'] = Product.objects.get(pk=data['product']).title
            data['price'] = Product.objects.get(pk=data['product']).price
            try:
                data['comment'] = CommentToOrder.objects.get(user=data['user']).text
            except:
                data['comment'] = None
            data['total'] = data['count'] * Product.objects.get(pk=data['product']).price
            new_list_data.append(data)
        return Response(new_list_data)


class UpdateDestroyUserRoleAPIView(GenericAPIView):
    permission_classes = (IsAdminPermission, IsAuthenticated)
    serializer_class = UserRoleSerializer

    def patch(self, request, user):
        user_role = UserRole.objects.get(user=user)
        serializer_user_role = self.get_serializer(user_role, request.data, partial=True)
        serializer_user_role.is_valid(raise_exception=True)
        serializer_user_role.save()
        return Response(serializer_user_role.data)


