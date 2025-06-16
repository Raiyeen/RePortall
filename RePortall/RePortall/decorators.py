from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    """
    Decorator to restrict access to authenticated users.
    Redirects to the login page if the user is authenticated.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('review')  # Redirect to review page if authenticated
        return view_func(request, *args, **kwargs)
    
    return wrapper