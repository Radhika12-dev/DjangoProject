from django.contrib import admin
from.models import Listing, LikedListing

#optional step to customize the admin interface for the Listing model
class ListingAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin interface which can be read only , we can't edit
    readonly_fields = ('id', 'vin')

admin.site.register(Listing, ListingAdmin)  # Register the Listing model with the admin site

class LikedListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'vin')

admin.site.register(LikedListing)


