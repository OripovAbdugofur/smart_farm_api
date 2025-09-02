from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sensors', views.SensorViewSet)
router.register(r'sensor-data', views.SensorDataViewSet)
router.register(r'devices', views.DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]