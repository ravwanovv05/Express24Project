from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from express.models.categories import Category
from express.models.products import Product, ShoppingCart
from express.serializers import CategorySerializer, ProductSerializer, ShoppingCartSerializer, \
    IncrementDecrementSerializer


class CategoryGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request):
        category = Category.objects.all().order_by('-created_at')
        serializer_category = self.get_serializer(category, many=True)
        return Response(serializer_category.data)


class ProductGenericAPIView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, category):
        product = Product.objects.filter(Q(category=category)).all()
        serializer_product = self.get_serializer(product, many=True)
        return Response(serializer_product.data)


class ShoppingCartGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShoppingCartSerializer

    def get(self, request):
        user = request.user
        shopping_cart = ShoppingCart.objects.filter(Q(user=user))
        serializer_shopping_cart = self.get_serializer(shopping_cart, many=True)
        list_data = serializer_shopping_cart.data
        list_new_data = []
        for data in list_data:
            data['image'] = Product.objects.get(Q(pk=data['product'])).image.url
            data['price'] = Product.objects.get(Q(pk=data['product'])).price
            data['total'] = data['count'] * Product.objects.get(Q(pk=data['product'])).price
            list_new_data.append(data)
        return Response(list_new_data)

    def post(self, request):
        serializer_shopping_cart = self.get_serializer(data=request.data)
        serializer_shopping_cart.is_valid(raise_exception=True)
        serializer_shopping_cart.save()
        return Response(serializer_shopping_cart.data)


class UpdateDestroyShoppingCartGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShoppingCartSerializer

    def patch(self, request, pk):
        shopping_cart = ShoppingCart.objects.get(pk=pk)
        serializer_shopping_cart = self.get_serializer(shopping_cart, request.data, partial=True)
        serializer_shopping_cart.is_valid(raise_exception=True)
        serializer_shopping_cart.save()
        return Response(serializer_shopping_cart.data)

    def delete(self, request, pk):
        shopping_cart = ShoppingCart.objects.get(pk=pk)
        try:
            shopping_cart.delete()
        except Exception as e:
            return Response({"success": False, 'message': str(e)}, status=404)
        return Response(status=204)


class IncrementShoppingCartGenericAPIVIew(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IncrementDecrementSerializer

    def patch(self, request, pk):
        shopping_cart = ShoppingCart.objects.get(pk=pk)
        increment_product = shopping_cart.count + 1
        print(increment_product)
        serializer_shopping_cart = self.get_serializer(shopping_cart, {'count': increment_product}, partial=True)
        serializer_shopping_cart.is_valid(raise_exception=True)
        serializer_shopping_cart.save()
        return Response(serializer_shopping_cart.data)


class DecrementShoppingCartGenericAPIVIew(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IncrementDecrementSerializer

    def patch(self, request, pk):
        shopping_cart = ShoppingCart.objects.get(pk=pk)
        decrement_product = shopping_cart.count - 1
        if decrement_product == 0:
            shopping_cart.delete()
            return Response(status=204)
        print(decrement_product)
        serializer_shopping_cart = self.get_serializer(shopping_cart, {'count': decrement_product}, partial=True)
        serializer_shopping_cart.is_valid(raise_exception=True)
        serializer_shopping_cart.save()
        return Response(serializer_shopping_cart.data)
