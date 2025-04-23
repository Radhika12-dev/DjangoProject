from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilters
from importlib import reload

def main_view(request):
    return render(request, 'views/main.html', {"name": "AutoMax"})

@login_required  # This decorator ensures that the user must be logged in to access the home view
def home_view(request):
    listings = Listing.objects.all()# Fetch all listings from the database
    # Apply filters to the listings based on the request parameters
    listing_filter = ListingFilters(request.GET, queryset=listings)
    context = {
        'listing_filter': listing_filter,  # Pass the filtered listings to the template context 
    }
    return render(request, 'views/home.html', context=context)

@login_required  # This decorator ensures that the user must be logged in to access the about view
def list_view(request):
    if request.method == 'POST':
        # Handle the form submission for creating a new listing
        try:
            #request.FILES #handle the uploaded files
            #request.POST #handle the form data
            listing_form = ListingForm(request.POST, request.FILES)  # Create a form instance with the submitted data
            location_form = LocationForm(request.POST)  # Create a form instance for the location
            if listing_form.is_valid() and location_form.is_valid():
                # Save the listing and location data but do not commit to the database yet 
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location  # Set the location for the listing
                listing.save()
                messages.info(request, f'{listing.model} Listing Created!')
                return redirect ('home')  # Redirect to the home page after successful form submission

            else:
                raise Exception("Form is not valid")
        except Exception as e:
            print(e)
            messages.error(request, "An error ocured while creating the listing.")
        
    elif request.method == 'GET':
        # Handle the form submission for creating a new listing
        listing_form = ListingForm()
        location_form = LocationForm()

    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form': location_form})  # Render the list.html template with the listing form

@login_required  # This decorator ensures that the user must be logged in to access the listing view
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)  # Fetch the listing object based on the provided ID 
        print(id)
        if listing is None:
            raise Exception("Listing not found")
        return render(request, 'views/listing.html', {'listing':listing})  # Render the listing.html template
    except Exception as e:
        return redirect('home')  # Redirect to the home page if the listing is not found or any other error occurs
    
@login_required
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        if request.method == 'POST':
            listing_form = ListingForm(request.POST, instance=listing)
            location_form = LocationForm(request.POST, instance=listing.location)
            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.info(request, f"Listing {id} updated successfully!")
                return redirect('home')
            else:
                messages.error(
            request, f"An error uccured while trying to update")
                return reload()
        
        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
        return render(request, "views/edit.html", {"location_form":location_form,
                                                   "listing_form": listing_form})
    except Exception as e:
        messages.error(
            request, f"An error uccured while trying to update"
        )
        return redirect('home')
    