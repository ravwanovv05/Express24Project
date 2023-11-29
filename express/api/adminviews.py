from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from express.serializers import CategorySerializer, ProductSerializer, UserSerializer
from users.models.roles import UserRole
from users.permissions import IsAdminPermission

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


class UserGenericAPIView(GenericAPIView):
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

