import random
from django.shortcuts import render,redirect
from django.core.mail import send_mail

from ecommerce_app.models import Seller1
from ecommerce_app.models import Customer
from django.conf import settings

# Create your views here.

def master(request):
    return render(request,'ecommerce_app/master.html')

def home(request):
    return render(request,'ecommerce_app/home.html')

def admin_login(request):
    return render(request,'ecommerce_app/admin_login.html')
    
def customer_signup(request):
    msg=''
    if request.method=='POST':
        customer_name=request.POST['name'].lower()
        customer_mobile=request.POST['mobileno']
        customer_mail=request.POST['email']
        customer_password=request.POST['password']
        customer_exist = Customer.objects.filter(customermail= customer_mail).exists()
        if not customer_exist:
          new_customer=Customer(
            customername=customer_name,
            customermobile=customer_mobile,
            customermail=customer_mail,
            customerpassword=customer_password

        )
        new_customer.save()
        msg='Account Registerd Succesfully'
    else:
        msg='Account already Exists'
        
    return render(request,'ecommerce_app/customer_signup.html',{'message': msg})

def customer_login(request):
    msg=''
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        try:
            customer = Customer.objects.get(customermail = email , customerpassword = password)
            request.session['customer'] = customer.id
            return redirect('customer_app:home')
        except:
            msg='incorrect'

    return render(request,'ecommerce_app/customer_login.html',{'message':msg})

def seller_login(request):
    msg = ''
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        try:
            seller = Seller1.objects.get(username = user_name, password = password)
            request.session['seller'] = seller.id
            return redirect('seller_app:home')
        except:
            msg = 'Incorrect Username or Password'


    return render(request,'ecommerce_app/seller_login.html',{'message': msg})

def seller_signup(request):
    msg = ''
    if request.method =='POST':
        seller_name=request.POST['name'].lower()
        mobile_no=request.POST['mobileno']
        s_email=request.POST['email']
        co_name=request.POST['company']
        s_username=random.randint(1111,9999)
        s_password='sel-'+str(s_username)
        seller_ac_holder_name = request.POST['ac_holder_name']
        seller_ifsc = request.POST['ifsc']
        seller_branch = request.POST['branch']
        seller_ac_no = request.POST['ac_no']
        seller_gender = request.POST['gender']
        seller_image = request.FILES['image']

        seller_exist = Seller1.objects.filter(email = s_email).exists()

        if not seller_exist:

            new_seller = Seller1(
                sellername = seller_name,
                mobileno = mobile_no,
                email = s_email,
                companyname = co_name,
                username = s_username,
                password = s_password,
                ac_holder_name = seller_ac_holder_name,
                ifsc = seller_ifsc,
                branch = seller_branch,
                ac_no = seller_ac_no,
                gender = seller_gender,
                image = seller_image,
            )
            new_seller.save()
            msg = 'Account Created Succesfully'

        else:
            msg = 'Email Exist'

        # msg='Hi Your User Name '+str(s_username)+'and your password is'+s_password
        # send_mail(
        #     'username and password',
        #     msg,
        #      settings.EMAIL_HOST_USER,
        #     [s_email]
            
        # )


    return render(request,'ecommerce_app/seller_signup.html',{'message': msg})