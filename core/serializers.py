from djoser.serializers import UserSerializer


class UserCreateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["id", "email", "first_name", "last_name", "image"]
