import django_filters

from .models import GISFeature

class GISFeatureFilter(django_filters.FilterSet):
    class Meta:
        model = GISFeature
        fields = {
            'id' : ['exact'],
            'scientific_name': ['iexact', 'icontains'],
            'kingdom': ['iexact', 'icontains'],
            'phylum_class': ['iexact', 'icontains'],
            'family': ['iexact', 'icontains'],
            'genus': ['iexact', 'icontains'],
            'country': ['iexact', 'icontains'],
            'state_province': ['iexact', 'icontains'],
        }