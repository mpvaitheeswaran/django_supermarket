from django.urls import path
from . import views

urlpatterns = [
    path('',views.BoardList.as_view(),name='boards'),
    path('move/',views.moveProduct,name='update_kanban_column'),
    path('add/',views.addProductBoard,name='add_product_board'),
    path('myboards/',views.myProductsData,name='my_boards'),
    path('update/<int:pk>/',views.ProductUpdateView.as_view(),name='product_update_board'),
    path('delete/',views.deleteBoard,name='delete_board'),
    #For Notifications
    path('read_all/',views.readAllNotifications,name='mark_read_all'),
    path('read/<int:id>/',views.readNotification,name='mark_read'),
]