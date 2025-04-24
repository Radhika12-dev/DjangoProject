from django.db import models
from uuid import uuid4
from users.models import *
from .constants import CARS_BRANDS, TRANSMISSION_OPTIONS
from .utils import *

class Listing(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)  # Unique identifier for each listing
   created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the listing was created
   updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the listing was last updated
   seller = models.ForeignKey(Profile, on_delete=models.CASCADE)  # Foreign key to the seller (user)
   brand = models.CharField(max_length=24, choices=CARS_BRANDS, default=None)  # Brand of the item
   model = models.CharField(max_length=64)  # Model of the item
   vin = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number (VIN)
   mileage = models.PositiveIntegerField(default=0)  # Mileage of the item
   color = models.CharField(max_length=24)  # Color of the item
   description = models.TextField()  # Description of the item
   engine = models.CharField(max_length=64)  # Engine type of the item
   transmission = models.CharField(max_length=24, choices=TRANSMISSION_OPTIONS, default=None)  # Transmission type of the item
   location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)  # Location of the item
   image = models.ImageField(upload_to=user_listing_path, blank=True, null=True)  # Image of the item

   def __str__(self):
      return f'{self.seller.user.username}\'s listing - {self.model}'

class LikedListing(models.Model):
   profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
   listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
   like_date = models.DateTimeField(auto_now_add=True)

   def __str__ (self):
      return f'{self.listing.model} listing liked by {self.profile.user.username}'

