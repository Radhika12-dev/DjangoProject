from django.urls import path
from .views import *
urlpatterns = [
    path('', main_view, name='main'),
    path('home/', home_view, name='home'),  # URL for the home page 
]