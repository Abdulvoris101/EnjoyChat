import re
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("home")
    return render(request, 'app_auth/register.html', {'form': form})


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'app_auth/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

def log_out(request):
    
    logout(request)
    return redirect('login')