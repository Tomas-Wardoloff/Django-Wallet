from django.db.models import Q
from django.db import IntegrityError

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            return Response(
                {'detail': 'Account with this user and name already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValidationError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
