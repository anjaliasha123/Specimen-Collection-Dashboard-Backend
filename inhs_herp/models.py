# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# Create your models here.
class GISFeature(models.Model):
    PHYLUM_CLASS_CHOICES = [
        ('Amphibia', 'Amphibia'),
        ('Reptilia', 'Reptilia'),
    ]
    id = models.IntegerField(primary_key=True)
    kingdom = models.CharField(max_length=255)
    phylum = models.CharField(max_length=255)
    phylum_class = models.CharField(max_length=255, choices=PHYLUM_CLASS_CHOICES, default='Amphibia')
    family = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    genus = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    decimal_latitude = models.DecimalField(max_digits=22, decimal_places=16)
    decimal_longitude = models.DecimalField(max_digits=22, decimal_places=16)

    # Geometry field
    geom = models.PointField(srid=4326, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.decimal_latitude and self.decimal_longitude:
            self.geom = Point(float(self.decimal_longitude), float(self.decimal_latitude), srid=4326)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.scientific_name