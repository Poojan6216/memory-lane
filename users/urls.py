from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import profile_view
from .views import custom_login

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    #path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('login/', custom_login, name='login'),
]
