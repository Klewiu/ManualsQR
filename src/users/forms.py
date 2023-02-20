from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_superuser = forms.BooleanField(
        required=False,
        label="Użytkownik z uprawnieniami administratora.",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_superuser']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    is_superuser = forms.BooleanField(
        required=False,
        label="Użytkownik z uprawnieniami administratora.",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser']