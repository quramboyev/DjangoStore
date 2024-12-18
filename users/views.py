from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    context = {'form': UserLoginForm() }
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            form = UserRegistrationForm()

    form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

def profile(request):
    form = UserProfileForm(isinstance=request.user)

    context = {
        'title': 'Store - Профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)