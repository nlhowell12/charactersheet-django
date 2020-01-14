from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'login', UserViewSet, basename='login')
urlpatterns = router.urls
