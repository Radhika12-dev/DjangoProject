import django_filters
from .models import Listing

class ListingFilters(django_filters.FilterSet):
    """
    FilterSet for Listing model.
    """
    class Meta:
        model = Listing
        fields = {
            'brand': ['exact'],
            'transmission': ['exact'],
            'mileage': ['lt'], #less than , but we can pass more than one filter
            'model': ['icontains'], #contains
    
            }