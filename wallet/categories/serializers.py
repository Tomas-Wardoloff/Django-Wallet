from rest_framework import serializers

from authentication.serializers import CustomUserSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Category
        fields = '__all__'
