from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.http import JsonResponse, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User


# User DB 확인 테스트
def user_view(request):
    users = User.objects.all()
    return render(request, 'index.html', {"users": users})


# 홈 화면
def home(request):
    return render(request, "home.html")


# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request, id=username, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'login.html')


# https://velog.io/@psj0810/django-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EA%B3%BC-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B5%AC%ED%98%84
# https://velog.io/@junnoli/DjangoMYSQL-%EB%A1%9C%EA%B7%B8%EC%9D%B8


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')


# 회원가입
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# 이모티콘 제작
def emo_create(request):
    return render(request, "emo_create.html")


# 이모티콘 공유 게시판
def emo_board(request):
    return render(request, "emo_board.html")


# 채팅
def chat(request):
    return render(request, "chat.html")


# 나만의 이모티콘
def my_emo(request):
    return render(request, "my_emo.html")
