from django.urls import path
from . import views

urlpatterns = [
    path('',views.BoardList.as_view(),name='boards'),
]