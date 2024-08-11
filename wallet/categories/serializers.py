from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Category
from authentication.serializers import UserEmailSerializer


class CategorySerializer(serializers.ModelSerializer):
    user = UserEmailSerializer(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        name = attrs.get('name')
        category_type = attrs.get('type')

        if Category.objects.filter(user=user, name=name, type=category_type).exists():
            raise ValidationError(
                "Category with this User, Name and Type already exists.")

        return attrs
