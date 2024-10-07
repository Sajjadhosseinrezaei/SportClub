from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserLoginForm
from django.views import View
from .models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class RegisterView(View):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(name=cd['name'], email=cd['email'], password=cd['password2'])
            messages.success(request, "you registered!", 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "you login", 'success')
                return redirect('home:home')
            messages.error(request, "Email or password is wrong!")
        return render(request, self.template_name, {'form': form})


class LogoutView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "you logout!")
        return redirect('home:home')

