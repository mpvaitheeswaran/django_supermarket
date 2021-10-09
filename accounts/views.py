from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy

# Create your views here.

class UserRegister(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('home')
        return super().get(request, *args, **kwargs)

class UserLogin(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('home')
        return super().get(request, *args, **kwargs)
