from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.models.user_model import User
from users.serializers import UserSerializer, ChangePasswordSerializer


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
            existing_user_username = User.objects.filter(Q(username=username))
            return Response({'success': False, 'message': 'This username already exists!'}, status=400)
        except User.DoesNotExist:
            pass

        try:
            existing_user_email = User.objects.filter(Q(email=email))
            return Response({'success': False, 'message': 'This email already exists!'}, status=400)
        except User.DoesNotExist:
            pass

        serializer_user = self.get_serializer(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        serializer_user.save()
        return Response(serializer_user.data)


class ChangePasswordUpdateAPIView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password!"]}, status=400)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password update successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=400)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
