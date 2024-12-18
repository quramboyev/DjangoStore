from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите фамилию'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите адрес эл. почты'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль'
    }))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'readonly': True
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'readonly': True
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image' 'username', 'email')

