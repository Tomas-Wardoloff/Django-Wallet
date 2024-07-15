from django.shortcuts import redirect


def redirect_to_login(request):
    """
    Redirects the user to the login page.
    """
    return redirect('login')
