from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from users.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterGenericAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        if password != confirm_password:
            return Response({'success': False, 'message': 'Passwords are not same!'})

        try:
            existing_user_username = User.objects.get(Q(username=username))
            return Response({'success': False, 'message': 'This username already exists!'}, status=400)
        except User.DoesNotExist:
            pass

        try:
            existing_user_email = User.objects.get(Q(email=email))
            return Response({'success': False, 'message': 'This email already exists!'}, status=400)
        except User.DoesNotExist:
            pass

        serializer_user = self.get_serializer(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        serializer_user.save()
        return Response(serializer_user.data)


