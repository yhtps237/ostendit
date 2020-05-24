from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from shows.models import Shows
from django.db import IntegrityError
from .forms import RegistrationForm
# Create your views here.


def signup_view(request):
    form = RegistrationForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == "GET":
        return render(request, 'user/signup.html', context)
    else:
        try:
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 == password2:
                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=firstname, last_name=lastname)
                # user = authenticate(username=username, password=password1)
                login(request, user)
                return redirect(f'/user/{user}')
            else:
                return render(request, 'user/signup.html', context)
        except IntegrityError:
            # context['error'] = 'This username has already been taken. Please use a new one.'
            return render(request, 'user/signup.html', context)


def login_view(request):
    form = AuthenticationForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'user/login.html', context)
    else:
        # if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'user/login.html', {'form': AuthenticationForm(request.POST or None), 'my_error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect(f'/user/{user}')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')


def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    if request.user.is_authenticated:
        objs = Shows.objects.filter(user__username__exact=username)
    else:
        objs = Shows.objects.filter(user__username__exact=username)[:2]
    context = {
        'user': user,
        'queryset': objs
    }
    return render(request, 'user/user_profile.html', context)
