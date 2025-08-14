from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_roles(allowed=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.profile.role in allowed:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Unauthorized Access")
        return wrapper_func
    return decorator
