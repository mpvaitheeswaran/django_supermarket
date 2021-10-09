from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.UserLogin.as_view(),name='login'),
    path('register/',views.UserRegister.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
]