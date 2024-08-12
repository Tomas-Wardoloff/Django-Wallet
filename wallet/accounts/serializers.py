from rest_framework import serializers

from .models import Account
from authentication.serializers import UserEmailSerializer


class AccountSerializer(serializers.ModelSerializer):
    user = UserEmailSerializer(read_only=True)

    class Meta:
        model = Account
        fields = '__all__'
