from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
# AuthenticationForms are used for user login forms in Django
from django.contrib.auth.forms import AuthenticationForm

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
