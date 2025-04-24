from django.urls import path
from .views import *
urlpatterns = [
    path('', main_view, name='main'),
    path('home/', home_view, name='home'),  # URL for the home page 
    path('list/', list_view, name='list'),  # URL for the listings page
    #<str:id> is a placeholder for the listing ID in the URL also called URL parameter.
    path('listing/<str:id>/', listing_view, name='listing'),  # URL for the listing details page
    path('listing/<str:id>/edit/', edit_view, name="edit"),
    path('listing/<str:id>/like/', like_listing_view, name='like_listing'),
    path('Listing/<str:id>/inquire/', inquire_listing_view, name ="email")
]