from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm

# Create your views here.
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'


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
