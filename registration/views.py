from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate as aut, login as li, logout as lo

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, template_name='registration/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        authenticated = aut(username=user.username, password=password)
        if authenticated is not None:
            li(request, authenticated)
            return redirect('index')
        else:
            return HttpResponse('Not authenticated...')


def logout(request):
    lo(request)
    return redirect('/')