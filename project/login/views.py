from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    return render(request, './login/index.html')

def login(request):
    if request.session.get('loginFlag', None):
        return redirect('/')
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if email and password:
            user = models.User.objects.filter(email=email)
            if user:
                _password = user[0].password
            else:
                return render(request, './login/login.html')
            if password == _password:
                request.session['loginFlag'] = True
                request.session['username'] = user[0].name
                return redirect('/')
            else:
                return render(request, './login/login.html')
    return render(request, './login/login.html')

def register(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        name = request.POST.get('name', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        if password1 == password2:
            user = models.User.objects.filter(email=email)
            if user:
                print("帳戶已經被註冊，請重新註冊")
                return redirect("/register/")
        new_user = models.User.objects.create()
        new_user.email = email
        new_user.name = name
        new_user.password = password1
        new_user.save()
        return redirect("/login/")
        
    return render(request, './login/register.html')

def logout(request):
    if request.session.get('loginFlag', None):
        request.session.flush()
        return redirect('/login/')
    return redirect('/')