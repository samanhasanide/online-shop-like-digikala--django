from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import Loginform
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="accounts/login.html",
         authentication_form=Loginform, redirect_authenticated_user=False), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile')

]
