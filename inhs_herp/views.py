from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import GISFeature
from .serializers import GISFeatureSerializer
from .pagination import GISFeaturePagination
from .filters import GISFeatureFilter
# Create your views here.


class GISFeatureViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = GISFeature.objects.all()
    serializer_class = GISFeatureSerializer
    pagination_class = GISFeaturePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = GISFeatureFilter
    search_fields = ['id', 'scientific_name', 'country', 'state_province', 'family', 'kingdom', 'genus']