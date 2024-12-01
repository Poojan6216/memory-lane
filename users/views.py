from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileForm
from .models import CustomUser
from django.contrib import messages



#@login_required
#def profile(request):
 #   return render(request, 'users/profile.html')


#def signup(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            user = form.save()  # Save the new user to the database
#            login(request, user)  # Log the user in automatically
#            return redirect('timeline')  # Redirect to the timeline
#    else:
#        form = UserCreationForm()  # Display an empty form
#    return render(request, 'registration/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
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