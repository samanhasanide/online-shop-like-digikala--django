from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registerforms, Loginform, UpdatePasswordForm, AddressForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from shop.models import Customer, Address


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = registerforms(request.POST)

            if form.is_valid():

                user = form.save()

                Customer.objects.create(
                    user=user,
                    phone=''
                )

                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']

                user = authenticate(
                    request,
                    username=username,
                    password=password1
                )

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


@login_required
def profile(request):

    customer = Customer.objects.get(user=request.user)

    if request.method == 'POST':

        action = request.POST.get('action')
        # Add Address

        if action == 'add_address':

            if customer.addresses.count() >= 2:
                return redirect('profile')

            form = AddressForm(request.POST)

            if form.is_valid():
                address = form.save(commit=False)
                address.customer = customer
                address.save()

                return redirect('profile')

        # Edit Address

        elif action == 'edit_address':

            address_id = request.POST.get('address_id')

            address = customer.addresses.get(id=address_id)

            form = AddressForm(
                request.POST,
                instance=address
            )

            if form.is_valid():
                form.save()

            return redirect('profile')

        # Edit User Information

        else:

            field = request.POST.get('field')
            value = request.POST.get('value')

            if field == 'first_name':
                request.user.first_name = value

            elif field == 'last_name':
                request.user.last_name = value

            elif field == 'email':
                request.user.email = value

            request.user.save()

            return redirect('profile')

    addresses = customer.addresses.all()

    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'customer': customer,
        'addresses': addresses,
        'address_form': AddressForm(),
    })


@login_required
def update_password(request):

    if request.method == 'POST':
        form = UpdatePasswordForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()

            update_session_auth_hash(request, user)

            return redirect('profile')

    else:
        form = UpdatePasswordForm(request.user)

    return render(request, 'accounts/update_password.html', {'form': form})
