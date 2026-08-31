from rest_framework.routers import DefaultRouter

from operations.api.views import OperationViewSet


router = DefaultRouter()

router.register("operations", OperationViewSet, basename="operation")

urlpatterns = router.urls
