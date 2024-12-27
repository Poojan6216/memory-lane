from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileForm
from .models import CustomUser
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout





def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if email not in settings.AUTHORIZED_USERS:
                form.add_error('email', 'This email is not authorized to register.')
                return render(request, 'registration/signup.html', {'form': form})
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in automatically
            return redirect('timeline')  # Redirect to the timeline
    else:
        form = CustomUserCreationForm()  # Display an empty form
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('timeline')  # Redirect to the same page after saving
        else:
            print("Form errors:", form.errors)

    else:
        form = ProfileForm(instance= user)

    return render(request, 'users/profile.html', {'form': form, 'user': user})


def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if email exists in the database
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.error(request, 'Email address not found.')
            return redirect('password_reset')

        # Check if passwords match
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('password_reset')

        # Set the new password
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Password reset successful! You can now log in with your new password.')
        return redirect('login')

    return render(request, 'users/password_reset.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.email in settings.AUTHORIZED_USERS:
            login(request, user)
            return redirect('timeline')  # Redirect to timeline or your desired page
        else:
            return render(request, 'unauthorized.html', {'message': 'You are not authorized to access this site.'})
    return render(request, 'login.html')  # Use your login page template