from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
# Create your views here.

# HW 6
from django.contrib.auth.models import User

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        
    return render(request, "users/login.html")


def logout_user(request):
    
    logout(request)
    
    return redirect("home")


# HW 6
def register_user(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            return render(
                request,
                "users/register.html",
                {"error": "Пароли не совпадают"}
            )

        if User.objects.filter(username=username).exists():
            
            return render(
                request,
                "users/register.html",
                {"error": "Пользователь уже существует"}
            )

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("login")

    return render(request, "users/register.html")