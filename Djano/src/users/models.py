from django.db import models
from django.contrib.auth.models import User
from localflavor.in_.models import INStateField
from django.core.validators import RegexValidator
from .utils import user_directory_path


class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = INStateField(default='HR') #InStateField is used to validate Indian state codes.
    postal_code = models.CharField(
        max_length=6,
        blank=True,
        validators=[RegexValidator(r'^\d{6}$', 'Enter a valid 6-digit postal code.')]
    )  # RegexValidator is used to validate the postal code format.

    def __str__(self):
        return f'Location {self.id}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The upload_to parameter specifies the directory where the uploaded file will be stored.
    # The user_directory_path function is used to create a dynamic path based on the user's ID.
    photo = models.ImageField(upload_to = user_directory_path, null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    
    # This method is called when the object is printed or converted to a string.
    # It returns a string representation of the object.
    # Earlier without this method, if we create the profile then it will show as Profile object 1, Profile object 2 etc.
    # But now it will show as username's Profile.
    def __str__ (self):
        return f'{self.user.username}\'s Profile'



    
