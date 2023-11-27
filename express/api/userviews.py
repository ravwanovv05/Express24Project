from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from express.models.categories import Category
from express.serializers import CategorySerializer


class CategoryGenericAPIView(GenericAPIView):
    serializer_class = (CategorySerializer,)

    def get(self, request):
        category = Category.objects.all().order_by('-created_at')
        serializer_category = self.get_serializer(category, many=True)
        return Response(serializer_category.data)
