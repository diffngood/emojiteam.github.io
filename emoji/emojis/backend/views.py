from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.


def user_view(request):
    users = User.objects.all()
    return render(request, 'index.html', {"users": users})


def home(request):
    return render(request, "home.html")


def login(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_msg = 'Invalid username or password'
    else:
        error_msg = 'error'
    return render(request, 'login.html', {'error': error_msg})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def emo_create(request):
    return render(request, "emo_create.html")


def chat(request):
    return render(request, "chat.html")
