from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the desired page after successful login
                return redirect('home')  # Replace 'home' with your desired URL name
            else:
                form.add_error(None, 'Invalid username or password.')

    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'dashboard/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                form.add_error('confirm_password', 'Passwords do not match')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'dashboard/register.html', context)

def base_view(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'dashboard/base.html', context)

def index(request):
    return render(request, 'dashboard/index.html')

def profile(request):
    # Handle profile page logic here
    return render(request, 'dashboard/profile.html')

def explore(request):
    # Handle explore page logic here
    return render(request, 'dashboard/explore.html')
