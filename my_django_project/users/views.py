from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

# Create your views here.

def singup_user(request):
    if request.user.is_authenticated:
        return redirect(to='quotes_and_authors:main')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_and_authors:main')
        else:
            return render(request, 'users/singup.html', {'form': form})
    
    return render(request, 'users/singup.html', {'form': RegisterForm()})

def login_user(request):
    if request.user.is_authenticated:
        return redirect(to='quotes_and_authors:main')
    
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return redirect(to='users:login')
        
        login(request, user)
        return redirect(to='quotes_and_authors:main')
    
    return render(request, 'users/login.html', {'form': LoginForm()})

@ login_required
def logout_user(request):
    logout(request)
    return redirect(to='quotes_and_authors:main')
