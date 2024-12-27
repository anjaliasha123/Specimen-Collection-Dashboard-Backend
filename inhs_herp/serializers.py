from rest_framework import serializers
from .models import GISFeature

class GISFeatureSerializer(serializers.ModelSerializer):

    type = serializers.CharField(default="Feature")
    geometry = serializers.SerializerMethodField()
    properties = serializers.SerializerMethodField()

    class Meta:
        model = GISFeature
        fields = ['type', 'geometry', 'properties']

        def get_geometry(self, obj: GISFeature):
            return {
                "type" : "Point",
                "coordinates": [float(obj.decimal_longitude), float(obj.decimal_latitude)]
            }
        
        def get_properties(self, obj: GISFeature):
            return {
                'id' : obj.id,
                'kingdom': obj.kingdom,
                'phylum': obj.phylum, 
                'phylum_class': obj.phylum_class, 
                'family': obj.family, 
                'scientific_name': obj.scientific_name, 
                'genus': obj.genus, 
                'country': obj.country, 
                'state_province': obj.state_province,
            }