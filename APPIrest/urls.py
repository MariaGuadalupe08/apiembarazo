from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerfilUsuarioViewSet,CalendarioViewSet, DesarrolloBebeViewSet, SintomasMamaViewSet, EjercicioViewSet

router = DefaultRouter()
router.register(r'perfil-usuario', PerfilUsuarioViewSet)
router.register(r'calendario', CalendarioViewSet)
router.register(r'desarrollo-bebe', DesarrolloBebeViewSet)
router.register(r'sintomas-mama', SintomasMamaViewSet)
router.register(r'ejercicios', EjercicioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
