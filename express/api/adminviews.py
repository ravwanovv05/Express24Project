from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from express.serializers import CategorySerializer, ProductSerializer, PictureSerializer
from users.permissions import IsAdminPermission


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


class AddPictureGenericAPIView(GenericAPIView):
    permission_classes = (IsAdminPermission, IsAuthenticated)
    serializer_class = PictureSerializer

    def post(self, request):
        serializer_picture = self.get_serializer(data=request.data)
        serializer_picture.is_valid(raise_exception=True)
        serializer_picture.save()
        return Response(serializer_picture.data)