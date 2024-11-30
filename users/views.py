from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileForm


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
