from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_process,logout as process_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from myapp.models import products1
from myapp.models import Category
from myapp.models import CartItem
from myapp.models import buyer


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

       

from django.db.models import Sum 
@login_required(login_url='login')
def home(request):
    all_products = products1.objects.all()
    
    # Initialize dictionaries to store products for each category
    electronic_products = []
    cosmetics_products = []
    groceries_products = []
    toys_products = []

    # Separate products into different categories based on conditions
    for product in all_products:
        if product.category.name == 'Electronic':
            electronic_products.append(product)
        elif product.category.name == 'Cosmetics':
            cosmetics_products.append(product)
        elif product.category.name == 'Groceries':
            groceries_products.append(product)
        elif product.category.name == 'Toys':
            toys_products.append(product)
        
    # Check if the user exists in the Seller table
    user_exists = Seller.objects.filter(name=request.user.username).exists()
    

# Step 1: Filter cart items with status 'ordered'
    cart_items = CartItem.objects.filter(status='ordered')

# Step 2: Group the cart items by product and calculate total quantity
    product_quantities = cart_items.values('product__product_id', 'product__name').annotate(total_quantity=Sum('quantity'))

# Step 3: Sort the product_quantities list based on total_quantity in descending order
    sorted_product_quantities = sorted(product_quantities, key=lambda item: item['total_quantity'], reverse=True)

# Step 4: Get the top 2 products with the maximum total quantity
    top_2_max_products = product_quantities.order_by('-total_quantity')[:6]
    #top_2_max_products = top_10_max_products[:2]

# Step 5: Retrieve the product objects for the top 2 products
    top_2_products = []
    for item in top_2_max_products:
     product_id = item['product__product_id']
     product = products1.objects.get(product_id=product_id)
     top_2_products.append(product)
    
#     current_username = request.user.username
    
#     cart_items1 = CartItem.objects.filter(status='ordered',buyer=current_username)
#     if(cart_items1!=None):
# # Step 2: Group the cart items by product and calculate total quantity
#      product_quantities1 = cart_items1.values('product__product_id', 'product__name').annotate(total_quantity=Sum('quantity'))

# # Step 3: Sort the product_quantities list based on total_quantity in descending order
#      sorted_product_quantities1 = sorted(product_quantities1, key=lambda item: item['total_quantity'], reverse=True)

# # Step 4: Get the top 2 products with the maximum total quantity
#     #top_2_max_products = product_quantities.order_by('-total_quantity')[:6]
#      top_2_max_products1 = product_quantities1.order_by('-total_quantity')[:300]

# # Extracting product IDs from the top 2 products
#      top_2_product_ids1 = [item['product__product_id'] for item in top_2_max_products1]

# # Retrieving products for the top 2 product IDs
#      top_2_products1 = products1.objects.filter(product_id__in=top_2_product_ids1)

# # Extracting category IDs from the top 2 products
#     # Extracting category names from the top 2 products
#    # top_2_category_names = top_2_products1.values_list('category__name', flat=True)
#     #top_2_category_names = top_2_products.values_list('category__name', flat=True).distinct()
#      top_2_category_names = []
#      for product in top_2_products1:
#       top_2_category_names.append(product.category.name)

# # Ensuring unique category names
#       top_2_category_names = list(set(top_2_category_names))

# # Retrieving categories for the extracted category names
#      #top_2_categories = Category.objects.get(name__in=top_2_category_names)
# # Retrieving categories for the extracted category names
#     #top_2_categories = Category.objects.filter(name__in=top_2_category_names)
# # Retrieving categories for the extracted category names
#      top_2_categories1 = []
#      for category_name in top_2_category_names:
#       categories = Category.objects.filter(name=category_name)

#      if categories!=None: 
#       for category in categories:
#         top_2_categories1.append(category.name)

#       top_5_products = []
#       for item in top_2_categories1:
#        current_username = request.user.username
     
#        cart_items = CartItem.objects.filter(product__category__name=item, status='ordered',buyer=current_username)

# # Group the cart items by product and calculate total quantity
#        product_quantities = cart_items.values('product__product_id', 'product__name').annotate(total_quantity=Sum('quantity'))

# # Sort the product_quantities list based on total_quantity in descending order
#     #sorted_product_quantities = sorted(product_quantities, key=lambda item: item['total_quantity'], reverse=True)
#        top_5_max_products = product_quantities.order_by('-total_quantity')[:12]
#        top_5_products=[]
#        for item in top_5_max_products:
#         product_id = item['product__product_id']
#         product = products1.objects.get(product_id=product_id)
#         top_5_products.append(product)

   # top_5_products=top_5_products1+top_5_products
# Get the top 5 products with the maximum total quantity
    #top_5_max_products = sorted_product_quantities[:5]

# Retrieve the product objects for the top 5 products
    
      


    return render(request, 'index.html', {
        'product_with_max_quantity': top_2_products,
       # 'top_5_products':top_5_products,
        'all_products': all_products,
        'electronic_products': electronic_products,
        'cosmetics_products': cosmetics_products,
        'groceries_products': groceries_products,
        'all_products': all_products,
        'toys_products':toys_products ,
        'user_exists': user_exists
        
    })


def logout(request):
    process_logout(request)
    return redirect('login')

def product_list(request):
    product = products1.objects.all()
    return render(request, 'product_list.html', {'products': product})

from django.shortcuts import render, HttpResponse
from .models import Seller, Category, products1
import json

from django.conf import settings
import os
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import products1

import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import products1

def add_product(request):
    if request.method == 'POST':
        # Extract product data from the form data
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category_name = request.POST.get('category')
        image = request.FILES.get('image')  # Access the uploaded image file

        # Get the current user's username
        current_username = request.user.username

        # Fetch the seller object using the username
        try:
            seller = Seller.objects.get(name=current_username)
        except Seller.DoesNotExist:
            return JsonResponse({"error": "Seller does not exist"}, status=400)

        # Fetch the category object using the category name
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category does not exist"}, status=400)

        # Create the product object
        product = products1(
            name=name,
            price=price,
            description=description,
            seller=seller,
            category=category,
            quantity=75,  # You may adjust this value as needed
            image=image
        )
        product.save()

        # Save the image to the media directory
        if image:
            # Define the directory to save the image
            image_directory = os.path.join(settings.MEDIA_ROOT, 'media')
            if not os.path.exists(image_directory):
                os.makedirs(image_directory)

            # Generate a unique file name
            image_name = f"{product.product_id}_{image.name}"

            # Write the image file to the directory
            with open(os.path.join(image_directory, image_name), 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # Set the image path in the product object
            product.image = os.path.join('media', image_name)
            product.save()
        else:
            return JsonResponse({"error": "Image is null"}, status=400)

        return HttpResponse("Product added successfully")
    else:
        categories = Category.objects.all()
        return render(request, 'add_product.html', {'categories': categories})





def shop(request):

    return render(request,'shop.html')

def shop_detail(request):
    all_products = products1.objects.all()
    
    # Initialize list to store electronic products
    
        
    electronic_products = []
    cosmetics_products = []
    groceries_products = []
    toys_products = []
    quantity1=0
    quantity2=0
    quantity3=0
    quantity4=0
    
    # Separate products into different categories based on conditions
    for product in all_products:
        if product.category.name == 'Electronic':
            electronic_products.append(product)
             # Calculate the quantity of electronic products
            quantity1 = len(electronic_products)

        elif product.category.name == 'Cosmetics':
            cosmetics_products.append(product)
            quantity2 = len(cosmetics_products)


        elif product.category.name == 'Groceries':
            groceries_products.append(product)
            quantity3 = len(groceries_products)

        
        elif product.category.name == 'Toys':
            toys_products.append(product)
            quantity4 = len(toys_products)

   
      
    return render(request, 'shop-detail.html', {
        'all_products': all_products,
        'electronic_products': electronic_products,
        'quantity1': quantity1,
        'quantity2': quantity2,
        'quantity3': quantity3,
        'quantity4': quantity4,
    })

def test(request):
    return render(request,'404.html')

def testimonial(request):
    return render(request,'testimonial.html')

def chackout(request):
      # Get the current user's username
    current_user = request.user.username

    # Retrieve cart items for the current user
    cart_items = CartItem.objects.filter(buyer=current_user, status='pending')

    # Calculate total price for each item according to quantity
    for item in cart_items:
        item.total_price = item.quantity * item.product.price

    # Calculate total price for all items in the cart
    total_price = sum(item.total_price for item in cart_items)

    return render(request,'chackout.html', {'cart_items': cart_items, 'total_price': total_price})

def contact(request):
    return render(request,'contact.html')

def search(request):
    product = products1.objects.all()
    return render(request, 'search.html', {'products': product})
    #return render(request,'search.html',{'allproduct':all_products})

from django.http import JsonResponse
from .models import products1

from django.http import JsonResponse
from .models import products1, Seller

def get_seller_products(request):
    # Assuming you have a way to identify the current seller
    current_seller_name = request.user.username  # Change this to fetch the current seller from the request
    
    try:
        current_seller = Seller.objects.get(name=current_seller_name)
    except Seller.DoesNotExist:
        return JsonResponse({'error': 'Seller not found'}, status=404)

    # Query products for the current seller
    seller_products = products1.objects.filter(seller=current_seller)

    # Convert products to JSON format
    products_data = []
    for product in seller_products:
        products_data.append({
            'image':product.image.url,
            'id':product.product_id, 
            'name': product.name,
            'price': product.price,
            'description': product.quantity,
            'category': product.category.name
            # Assuming you want to include the category name
            # Add other fields as needed
        })

    return JsonResponse({'products': products_data})
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        current_buyer_name = request.user.username 
        quantity = request.POST.get('quantity')
        cart_products = products1.objects.get(product_id=product_id)


       
        cartitem1= CartItem(
            buyer=current_buyer_name,
            product=cart_products,
            quantity=quantity

           
        )
        cartitem1.save()
        
        return JsonResponse({'status': 'success', 'message': 'Product added to cart'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
    

def cart_count(request):
    
    current_buyer_name = request.user.username 
    count=CartItem.objects.filter(buyer=current_buyer_name, status='pending').count()
    return JsonResponse({'count': count})

@login_required
@csrf_exempt
def cart(request):
    # Get the current user's username
    current_user = request.user.username

     # Retrieve cart items for the current user excluding items with status 'ordered'
    cart_items = CartItem.objects.filter(buyer=current_user, status='pending')

    # Calculate total price for each item according to quantity
    for item in cart_items:
        item.total_price = item.quantity * item.product.price

    # Calculate total price for all items in the cart
    total_price = sum(item.total_price for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

from django.http import JsonResponse
from .models import CartItem
@login_required
@csrf_exempt
def delete_cart_item(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.delete() # Delete the cart item from the database
            return JsonResponse({'success': True}) # Return success response
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Cart item not found'}) # Return error response if the cart item does not exist
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}) # Return error response for invalid request method
@login_required
@csrf_exempt   
def update_total_price(request):
    if request.method == 'GET':
        # Retrieve all cart items for the current user
        current_user = request.user.username
        cart_items = CartItem.objects.filter(buyer=current_user)
        
        # Calculate total price for all items in the cart
        total_price = sum(item.quantity * item.product.price for item in cart_items)
        
        return JsonResponse({'total_price': total_price}) # Return total price as JSON response
    else:
        return JsonResponse({'error': 'Invalid request method'}) # Return error response for invalid request method    
@login_required
@csrf_exempt 
def update_cart_item_quantity(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        new_quantity = int(request.POST.get('quantity', 0))  # Get the new quantity and convert it to an integer

        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            product = products1.objects.get(product_id=cart_item.product.product_id)  # Access the related product through the foreign key

            if new_quantity > product.quantity:
                # If the requested quantity exceeds the available stock
                return JsonResponse({
                    'success': False,
                    'error': 'Insufficient stock available',
                    'max_quantity': product.quantity
                })

            if new_quantity <= 0:
                # Handle cases where the quantity is zero or negative
                return JsonResponse({'error': 'Quantity must be greater than zero'})

            cart_item.quantity = new_quantity
            cart_item.save()
            return JsonResponse({'success': True, 'quantity': new_quantity})
        except CartItem.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'})
        except ValueError:
            return JsonResponse({'error': 'Invalid quantity value'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def checkout(request):
    return render(request,'chackout.html')


from .models import Order
@login_required
@csrf_exempt 
def submit_order(request):
    if request.method == 'POST':
        current_user = request.user.username 
         # Get the cart items for the current user
        cart_items = CartItem.objects.filter(buyer=current_user)
        # Change the status of each cart item to 'ordered'
        for item in cart_items:
            item.status = 'ordered'
            item.save()

# Create an Order from the POST data
        new_order = Order(
            username=current_user,
            first_name=request.POST.get('firstname', ''),
            last_name=request.POST.get('lastname', ''),
            company_name=request.POST.get('company', ''),
            address=request.POST.get('address', ''),
            town_city=request.POST.get('city', ''),
            country=request.POST.get('country', ''),
            postcode=request.POST.get('postcode', ''),
            mobile=request.POST.get('mobile', ''),
            email=request.POST.get('email', ''),
            order_notes=request.POST.get('ordernotes', ''),
            shipping=request.POST.get('shipping_method', ''),
            pay_method=request.POST.get('payment_method', '')
            
        )
        new_order.save()

        return JsonResponse({'success': True})
 # Redirect to a new URL if the order is successful
    else:
        # Render form again or show error
        return JsonResponse({'error': True})
    
def get_seller_productsd(request):
    # Assuming you have a way to identify the current seller
    current_seller_name = request.user.username  # Change this to fetch the current seller from the request
    
    try:
        current_seller = Seller.objects.get(name=current_seller_name)
    except Seller.DoesNotExist:
        return JsonResponse({'error': 'Seller not found'}, status=404)
    seller_cart_item_ids = CartItem.objects.filter(product__seller__name=current_seller, status='ordered').values_list('product_id', flat=True)

    # Query products for the current seller that have associated cart items with status 'ordered'
    seller_products = products1.objects.filter(seller=current_seller, product_id__in=seller_cart_item_ids)
    
    # Convert products to JSON format
    # Convert products to JSON format
    products_data = []
    for product in seller_products:
        products_data.append({
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category.name,  # Assuming you want to include the category name
            'prod_id':product.product_id
            # Add other fields as needed
        })

    return JsonResponse({'products': products_data})

def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            # Delete the product based on the received ID
            products1.objects.filter(product_id=product_id).delete()
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        except products1.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)