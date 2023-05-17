from django.urls import path
from .import views

app_name='ecommerce_app'

urlpatterns =[
    path('home',views.home,name='home'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('customer_signup',views.customer_signup,name='customer_signup'),
    path('master',views.master,name='master'),
    path('customer_login',views.customer_login,name='customer_login'),
    path('seller_login',views.seller_login,name='seller_login'),
    path('seller_signup',views.seller_signup,name='seller_signup'),

]