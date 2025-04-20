from .models import Profile, Location
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Create a Profile object for the new User
        profile = Profile.objects.create(user=instance)
        # Create a Location object and assign it to the Profile
        location = Location.objects.create()
        profile.location = location
        profile.save()