from rest_framework.routers import DefaultRouter
from .views import DoctorsViewSet

router = DefaultRouter()
router.register(r"doctors", DoctorsViewSet, basename="doctors")

urlpatterns = router.urls