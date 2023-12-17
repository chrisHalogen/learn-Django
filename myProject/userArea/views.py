from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exists')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Exists')

            else:
                #  Create the user
                user = User.objects.create(
                    username = username,
                    email = email,
                    password = password
                )

                user.set_password(password)

                user.is_active = True

                user.save()
                return redirect('login')
            
            return render(request, 'register.html')

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # print(username,password)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        
        else:
            messages.info(request, 'Invalid cridentials')
            return redirect('login')

    return render(request, 'login.html')

def dashboard(request):
    # if not request.user.is_authenticated:
    #     messages.info(request, 'You have to log in')
    #     return redirect('login')
    return render(request, 'dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect("login")