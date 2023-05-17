from django.shortcuts import render,redirect
from ecommerce_app.models import Seller1
from .models import Product
# Create your views here.

def seller_master(request):
    seller = Seller1.objects.get(id= request.session['seller'])
    return render(request,'seller_app/seller_master.html',{'seller':seller})
    

def add_product(request):
    msg=''
    if request.method =='POST':
        product_name = request.POST['p_name'].lower()
        description = request.POST['p_des']
        stock = request.POST['p_stock']
        code = request.POST['p_code']
        price = request.POST['p_price']
        image = request.FILES['p_image']
        product_exist = Product.objects.filter(seller = request.session['seller'],code = code).exists()


        if not product_exist:
            product = Product(
                product_name = product_name,
                description = description,
                stock = stock,
                code = code,
                price = price,
                image = image,
                seller_id = request.session['seller']

                
            )
            product.save()
            msg='Product Added Succesfully'

        else:
            msg = 'Product Exist'
 
    return render(request,'seller_app/add_product.html',{'message': msg})


def home(request):
    sellers = Seller1.objects.get(id= request.session['seller'])
    return render(request,'seller_app/home.html',{'seller':sellers})
    

def catalogue(request):
    products = Product.objects.filter(seller = request.session['seller'])
    return render(request,'seller_app/catalogue.html',{'products': products})
    
    
def update_stock(request):
    return render(request,'seller_app/update_stock.html')


def logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('ecommerce_app:seller_login')


def update_password(request):
    msg = ''
    if request.method == 'POST':
        current_password = request.POST['current_password']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            
            if len(password) >= 8:


                seller = Seller1.objects.get(id= request.session['seller'])

                if seller.password == current_password:

                    seller.password = confirm_password
                    seller.save()
                    
                    msg = 'Password changed succesfully'
                else:
                    msg = 'Invalid password'
            else:
                msg = 'password should be min 8 characters'
        else:
            msg = 'password does not match'

    return render(request,'seller_app/update_password.html',{'message': msg})
def edit(request):
    return render(request,'seller_app/edit_profile.html')