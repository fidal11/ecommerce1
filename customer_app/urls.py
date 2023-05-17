from django.urls import path
from .import views

app_name='customer_app'

urlpatterns =[
    path('home',views.home,name='home'),
    path('customer_master',views.customer_master,name='customer_master'),
    path('cart',views.cart,name='cart'),
    path('change_password',views.change_password,name='change_password'),
    path('logout',views.logout,name='logout'),
    path('demo',views.demo,name='demo')
    
]