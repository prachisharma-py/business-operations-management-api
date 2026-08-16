from rest_framework.routers import DefaultRouter

from departments.api.views import DepartmentViewSet


router = DefaultRouter()

router.register("deparments", DepartmentViewSet, basename="deparment")

urlpatterns = router.urls
