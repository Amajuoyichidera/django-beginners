from django.shortcuts import render
from .forms import LoginForm,UserRegistrationForm

# Create your views here.


def sign_up(request):
    form=UserRegistrationForm()
    context={
        'form':form
    }
    return render(request, 'users/signup.html', context)


def login_user(request):
    form=LoginForm()
    context={
        'form':form
    }
    return render(request, 'users/login.html', context)


def logout_user(request):
    pass