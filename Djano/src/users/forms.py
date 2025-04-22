from django import forms
from .models import Location

# These are the custom forms for the Location model.
class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    address_2 = forms.CharField(required=False)
    class Meta:
        model = Location
        fields = ['address_1', 'address_2', 'city', 'state', 'postal_code']
  # Include all fields from the Location model

    