from rest_framework import routers

from .views import (
    CustomUserViewSet,
    AccountViewSet,
    CategoryViewSet,
    TransactionViewSet,
    TransferViewSet)


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'transfers', TransferViewSet)

urlpatterns = router.urls
