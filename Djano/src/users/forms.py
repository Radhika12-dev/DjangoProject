from django import forms
from .models import Location, Profile
from django.contrib.auth.models import User

# These are the custom forms for the Location model.
class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    address_2 = forms.CharField(required=False)
    class Meta:
        model = Location
        fields = ['address_1', 'address_2', 'city', 'state', 'postal_code']
  # Include all fields from the Location model

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']  # Include all fields from the User model

class ProfileForm(forms.ModelForm):

    photo = forms.ImageField(required=False)
    phone = forms.CharField(required=True)
    class Meta:
        model = Profile
        fields = ['photo', 'bio', 'phone']


    