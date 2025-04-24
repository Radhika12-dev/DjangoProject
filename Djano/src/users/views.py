from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# AuthenticationForms are used for user login forms in Django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from .forms import LocationForm, UserForm, ProfileForm
from main.models import Listing, LikedListing

# Function Based View for User Login
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data = request.POST)
        if login_form.is_valid():
            # If the form is valid, authenticate the user and log them in
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            #authenticate will check the credentials against the user database
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                # success, faliure etc are the tags that are associated with the message
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, f"Invalid username or password.")
        else:
            messages.error(request, f"Invalid username or password.")
            # login_form = AuthenticationForm()
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login': login_form})  # Render the login template

@login_required 
def logout_view(request):
    logout(request)
    return render(request, 'views/main.html')  # Redirect to the main page after logout

#Class Based View for Registering a User
class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {'register': register_form})

    def post(self, request):
        register_form = UserCreationForm(data = request.POST)
        if register_form.is_valid():
            #UserCreationForm will automatically create a user instance and save it to the  user database
            user = register_form.save()
            user.refresh_from_db()  # Refresh the user instance from the database
            login(request, user)  # Log the user in
            messages.success(request, f"Registration successful. You are now logged in as {user.username}.")
            return redirect('home')
        else:
            messages.error(request, f"Invalid registration details.")
            return render(request, 'views/register.html', {'register': register_form})

#for class based views we need to use method_decorator to apply the login_required decorator     
@method_decorator(login_required, name='dispatch')  # Ensure the user is logged in to access this view
#This view is used to populate the profile, location and user db from fontend to backend
class ProfileView(View):

    def get(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=request.user.profile)
        locationform = LocationForm(instance=request.user.profile.location)
        return render(request,
                    'views/profile.html',
                    {'user_form':userform, 'profile_form': profileform,
                    'location_form': locationform,
                    'user_listings': user_listings,
                    'user_liked_listing': user_liked_listings})  # Render the profile template
    
    #As soon as we click save button all the data will be saved to the database after validation
    def post(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        locationform = LocationForm(request.POST, instance=request.user.profile.location)

        if userform.is_valid() and profileform.is_valid() and locationform.is_valid():
            userform.save()
            profileform.save()
            locationform.save()
            messages.success(request, f"Profile updated successfully.")
            return redirect('home')
        else:
            messages.error(request, f"Invalid profile details.")
            return render(request,
                        'views/profile.html',
                        {'user_form':userform, 'profile_form': profileform,
                        'location_form': locationform, 'user_listings': user_listings,
                        'user_liked_listing': user_liked_listings})
