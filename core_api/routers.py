from core_api.Viewsets.empleado_viewsets import EmpleadoViewSet
from rest_framework import routers
from .views import AutoViewSet, DireccionViewSet  

router = routers.DefaultRouter()

router.register(r'empleados', EmpleadoViewSet)
router.register(r'autos', AutoViewSet)
router.register(r'direcciones', DireccionViewSet)
