from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, EditProfileForm
from .models import User, TravelPlan
from .openai_utils import create_completion

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

def profile_view(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'dashboard/profile.html', context)

def explore(request):
    # Handle explore page logic here
    return render(request, 'dashboard/explore.html')

def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'dashboard/edit_profile.html', {'form': form})

def some_view(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        destination = request.POST.get('destination')
        duration = int(request.POST.get('duration'))
        preferences = request.POST.get('preferences')
        food_preferences = request.POST.get('food-preferences')
        interests = request.POST.get('interests')

        # Call the send_api_request function with the form data
        response_data = create_completion(destination, duration, preferences, food_preferences, interests)

        if response_data is not None:
            # API request was successful, create and save TravelPlan object
            travel_plan = TravelPlan(destination=destination, days=duration, api_response=response_data)
            travel_plan.save()
            # Optionally, you can add a success message here
            return redirect('profile')  # Replace 'profile' with the URL name of the profile page
        else:
            # API request failed, handle error (e.g., show an error message to the user)
            # Optionally, you can add an error message here
            return render(request, 'dashboard/profile.html')

    # If it's not a POST request, render the form page
    return render(request, 'form_page.html')