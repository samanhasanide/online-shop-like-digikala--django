from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from shop.models import Address


class UpdatePasswordForm(PasswordChangeForm):
    pass


class registerforms(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={"autofocus": True, 'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'password'}))


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['title', 'address']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Home'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full address',
                'rows': 3
            }),
        }
