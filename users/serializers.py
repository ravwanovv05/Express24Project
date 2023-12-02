from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer, CharField


User = get_user_model()


class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        ref_name = 'UserSerializer'
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user


class ChangePasswordSerializer(Serializer):
    model = User

    old_password = CharField(required=True)
    new_password = CharField(required=True)
