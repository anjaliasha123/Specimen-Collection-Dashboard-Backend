from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GISFeatureViewSet

VERSION = 'v1'

router = DefaultRouter()
router.register('gis', GISFeatureViewSet, basename='gis')

urlpatterns = [
    path('api/'+VERSION+'/', include(router.urls))
]
