from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    #This is how we can modify the model form to add custom fields or change the behavior of existing fields.
    image = forms.ImageField(required=False)  # Optional image field
    class Meta:
        model = Listing
        fields = ['image', 'brand', 'model', 'vin', 'mileage',
                  'color', 'engine', 'transmission', 'description' ] # Include all fields from the Listing model
        
        

