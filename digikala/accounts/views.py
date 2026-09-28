from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registerforms, Loginform
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = registerforms(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']
                user = authenticate(
                    request, username=username, password=password1)
                login(request, user)
                homeurl = reverse('home')
                return HttpResponseRedirect(homeurl)
            else:
                registerurl = reverse('register')
                return HttpResponseRedirect(registerurl)
        else:
            form = registerforms()

        return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    return render(request, 'accounts/login.html')


def logout_user(request):
    pass
