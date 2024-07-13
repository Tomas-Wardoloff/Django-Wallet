from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserLoginForm, CustomUserCreationForm


@csrf_protect
def user_login(request):
    """
    Handle the login process for a user.

    This view handles both GET and POST requests. For GET requests, it displays the login form.
    For POST requests, it attempts to authenticate the user with the provided email and password.
    If authentication is successful, the user is redirected to the home page. Otherwise, an error message
    is displayed.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object rendering the login page with the login form for GET requests or
        redirecting to the home page for successful POST requests.
    """
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = CustomUserLoginForm()
    return render(request, 'authentication/login.html', {'form': form})


@csrf_protect
def user_register(request):
    """
    Handle the user registration process.

    This view handles both GET and POST requests. For GET requests, it displays the registration form.
    For POST requests, it attempts to create a new user with the provided information. If the form
    data is valid and the user is successfully created, the user is redirected to the login page.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object rendering the registration page with the registration form for GET requests or
        redirecting to the login page for successful POST requests.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


@login_required
def user_logout(request):
    """
    Log out the current user.

    This view logs out the current user and redirects them to the login page. It requires that the user
    is already authenticated (login required).

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponseRedirect object redirecting to the login page.
    """
    logout(request)
    return redirect('login')
