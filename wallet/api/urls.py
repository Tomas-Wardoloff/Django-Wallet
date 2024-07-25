from rest_framework import routers

from .views import CustomUserViewSet


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = router.urls
