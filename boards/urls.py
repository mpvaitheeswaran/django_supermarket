from django.urls import path
from . import views

urlpatterns = [
    path('',views.BoardList.as_view(),name='boards'),
    path('move/',views.moveProduct,name='update_kanban_column'),
]