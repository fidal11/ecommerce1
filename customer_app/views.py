from django.shortcuts import render,redirect
from seller_app.models import Product
from ecommerce_app.models import Customer

def home(request):

    products = Product.objects.all()
    return render(request,"customer_app/home.html",{'products': products})

def customer_master(request):
    customer = Customer.objects.get(id= request.session['customer'])
    return render(request,'customer_app/customer_master.html',{'customer':customer})

def cart(request):
    return render(request,'customer_app/cart.html')

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect( 'ecommerce_app:home' )

def change_password(request):


    msg = ''
    if request.method == 'POST':
        current_password = request.POST['current_password']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            
            if len(password) >= 8:


                customer = Customer.objects.get(id= request.session['customer'])

                if customer.customerpassword == current_password:

                    Customer.objects.filter(id= request.session['customer']).update(customerpassword = confirm_password)
                    
                    msg = 'Password changed succesfully'
                else:
                    msg = 'Invalid password'
            else:
                msg = 'password should be min 8 characters'
        else:
            msg = 'password does not match'

     

    return render(request,'customer_app/change_password.html',{'message':msg})



def demo(request):
    products = Product.objects.all()
    return render(request,'customer_app/demo.html',{'products': products})