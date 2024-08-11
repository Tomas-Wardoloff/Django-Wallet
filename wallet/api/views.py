from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from accounts.models import Account
from accounts.serializers import AccountSerializer
from transactions.models import Transfer, Transaction
from transactions.serializers import TransactionSerializer, TransferSerializer
from categories.models import Category
from categories.serializers import CategorySerializer


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


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Category.objects.filter(Q(user=self.request.user) | Q(user__isnull=True))

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied(
                "User does not have permission to delete the category")
