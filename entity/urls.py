from django.urls import path, include
from rest_framework import routers
from .api import EntityViewSet
from django.conf.urls.static import static
from django.conf import settings

from . import views

router = routers.DefaultRouter()
router.register('api', EntityViewSet, 'api')

urlpatterns = [
    path('list', views.list, name='list'),
    path('<int:entityID>', views.single, name='entity'),
    path('api/<name>', EntityViewSet.as_view({'get': 'retrieve'})),
    path('api/<entityID>', EntityViewSet.as_view({'get': 'retrieve'})),
    path('api/<origin>', EntityViewSet.as_view({'get': 'filter'})),
    path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
