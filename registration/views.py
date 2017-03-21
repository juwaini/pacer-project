from django.http import HttpResponse
from registration.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate as aut, login as li, logout as lo

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, template_name='registration/register.html')

    else:  # for request.method == 'POST'
        context = {}

        user = User()
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('password-repeat')

        if password == password_again:
            user.set_password(password)
            user.save()
            profile = Profile(user=user)
            profile.save()
            return redirect('login')
        else:
            context['error'] = "Your password is not the same..."
            return render(request, template_name='registration/register.html', context=context)


def login(request):
    if request.method == 'GET':
        return render(request, template_name='registration/login.html')

    else:  # for request.method == 'POST'
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