from .views import *
from django.urls import path

urlpatterns = [
    path('login/', login_view, name='login'),  # URL for the login page
    path('register/', RegisterView.as_view(), name='register'),  # URL for the register page
    path('logout/', logout_view, name='logout'),  # URL for the logout page
    path('profile/', ProfileView.as_view(), name='profile'),  # URL for the profile page
]
