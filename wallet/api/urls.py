from rest_framework import routers

from .views import (
    CustomUserViewSet,
    AccountViewSet,
    CategoryViewSet,
    TransactionViewSet)


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = router.urls
