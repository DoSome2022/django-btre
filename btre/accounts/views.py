from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts/login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html',{'form':form})


def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password )

        if user is not None:
            login(request, user)
            messages.success(request,'You are logging in !')
            return redirect('dashboard')

    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')