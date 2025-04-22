from django.contrib import admin
from.models import Listing

#optional step to customize the admin interface for the Listing model
class ListingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing, ListingAdmin)  # Register the Listing model with the admin site

# Register your models here.
