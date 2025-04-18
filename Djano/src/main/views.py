from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def main_view(request):
    return render(request, 'views/main.html', {"name": "AutoMax"})