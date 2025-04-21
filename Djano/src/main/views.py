from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

def main_view(request):
    return render(request, 'views/main.html', {"name": "AutoMax"})

@login_required  # This decorator ensures that the user must be logged in to access the home view
def home_view(request):
    return render(request, 'views/home.html')