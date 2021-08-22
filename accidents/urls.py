from rest_framework.routers import DefaultRouter

from .views import AccidentViewSet

router = DefaultRouter()
router.register('accidents', AccidentViewSet, basename = 'accidents')

urlpatterns = []

urlpatterns += router.urls