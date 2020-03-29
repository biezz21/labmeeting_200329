from django.urls import path, include
from .views import PgllistViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pgl', PgllistViewset, basename='pgl')
urlpatterns = [
    path('test/', include(router.urls)),
    path('test/<int:pk>/', include(router.urls)),
]