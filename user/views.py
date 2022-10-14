from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth


# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')

        post_user = User()
        post_user.username = username
        post_user.password = password
        post_user.phone_number = phone
        post_user.address = address
        post_user.save()
        return redirect('/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/home')
        else:
            return render(request, 'login.html')


def home(request):
    user = request.user.is_authenticated

    if user:
        return render(request, 'home.html')
    else:
        return redirect('/login')
