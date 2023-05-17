from django.urls import path
from .import views

app_name='seller_app'

urlpatterns =[
    path('seller_master',views.seller_master,name='seller_master'),
    path('add_product',views.add_product,name='add_product'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),

    path('catalogue',views.catalogue,name='catalogue'),
    path('update_stock',views.update_stock,name='update_stock'),
    path('update_password',views.update_password,name='update_password'),
    path('edit',views.edit,name='edit'),





]