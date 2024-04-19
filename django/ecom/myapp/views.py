from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_process,logout as process_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from myapp.models import products1
# Create your views here.


def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login_process(request,user)
            return redirect('home')
        else:
            return HttpResponse("user not found")
    return render(request,'login.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Seller  # Make sure to import the Seller model
from .models import buyer
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        role = request.POST.get('role')  # Retrieve the role from POST data

        # Check if passwords match
        if pass1 != pass2:
            return HttpResponse("Your passwords do not match.")
        else:
            # Create a new user
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()

            # Check if the role is 'seller' and create a seller entry if it is
            if role == 'seller':
                new_seller = Seller(name=uname)  # Assuming name is sufficient for Seller, adjust if more fields
                new_seller.save()
            if role == 'buyer':
                new_buyer = buyer(name=uname)  # Assuming name is sufficient for Seller, adjust if more fields
                new_buyer.save()    

        return redirect('login')  # Redirect to login page after successful signup
    return render(request, 'signup.html')

       

   
@login_required(login_url='login')
def home(request):
    all_products = products1.objects.all()
    
    # Initialize dictionaries to store products for each category
    electronic_products = []
    cosmetics_products = []
    groceries_products = []

    # Separate products into different categories based on conditions
    for product in all_products:
        if product.category.name == 'Electronic':
            electronic_products.append(product)
        elif product.category.name == 'Cosmetics':
            cosmetics_products.append(product)
        elif product.category.name == 'Groceries':
            groceries_products.append(product)
    
    # Check if the user exists in the Seller table
    user_exists = Seller.objects.filter(name=request.user.username).exists()

    return render(request, 'index.html', {
        'electronic_products': electronic_products,
        'cosmetics_products': cosmetics_products,
        'groceries_products': groceries_products,
        'user_exists': user_exists
    })


def logout(request):
    process_logout(request)
    return redirect('login')

def product_list(request):
    product = products1.objects.all()
    return render(request, 'product_list.html', {'products': product})

def add_product(request):
    if request.method == 'POST':
        # Handle the form submission here, save the data to the database
        # Example: Assuming you have a Product model
        

        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        shop_name = request.POST.get('shop_name')
        print(name)
        product = products1(name=name, price=price, description=description, shopname=shop_name)
        product.save()

        

    return render(request, 'add_product.html')


def cart(request):

    return render(request,'cart.html')

def shop(request):

    return render(request,'shop.html')

def shop_detail(request):
    return render(request,'shop-detail.html')

def test(request):
    return render(request,'404.html')

def testimonial(request):
    return render(request,'testimonial.html')

def chackout(request):
    return render(request,'chackout.html')

def contact(request):
    return render(request,'contact.html')
