from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from accounts.models import Account
from accounts.serializers import AccountSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
