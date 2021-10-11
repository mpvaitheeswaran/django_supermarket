from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductList.as_view(),name='product_list'),
    path('me/',views.MyProductList.as_view(),name='my_product_list'),
    path('myproducts/',views.myProductsData,name='my_products'),
    # path('create/',views.ProductCreate.as_view(),name='product_create'),
    path('create/',views.ProductCreateView.as_view(),name='product_create'),
    path('read/<int:pk>', views.ProductReadView.as_view(), name='product_read'),
    path('update/<int:pk>/',views.ProductUpdateView.as_view(),name='product_update'),
    path('delete/<int:pk>/',views.ProductDeleteView.as_view(),name='product_delete'),
    path('delete/',views.deleteProduct,name='delete_products'),
]