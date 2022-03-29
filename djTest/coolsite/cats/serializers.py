from rest_framework import serializers
from rest_framework.fields import SkipField

from cats.models import User


class UserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    newField = serializers.CharField(default='QWErtBNewPQIWJre', read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    # def validate(self, attrs):
    #     print('VALODR', attrs)
    #     return attrs

    def validate_username(self, value):
        print("USERNAME___", value)
        return "USERNAME___" + value

    def create(self, validated_data):
        validated_data.pop('newField', False)
        return super().create(validated_data)
