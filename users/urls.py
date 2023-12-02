from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.api.views import RegisterGenericAPIView, ChangePasswordUpdateAPIView

urlpatterns = [
    path('register', RegisterGenericAPIView.as_view(), name='register'),
    path('change-password', ChangePasswordUpdateAPIView.as_view(), name='change_password'),
    # path('password-reset', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
