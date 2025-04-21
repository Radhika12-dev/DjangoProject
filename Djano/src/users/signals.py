from .models import Profile, Location
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
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

@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, **kwargs):
    # Delete the Location object when the Profile is deleted
    if instance.location is not None:
        instance.location.delete()