"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
 path('admin/', admin.site.urls),
    path('',views.signup,name='signup'),
    path('login/',views.login,name="login"),
path('home/',views.home,name="home"),
path('cart/',views.cart,name="cart"),
path('shop/',views.shop,name="shop"),
path('test/',views.test,name="test"),
# path('index/',views.test,name="index"),
path('testimonial/',views.testimonial,name="testimonial"),
path('chackout/',views.chackout,name="chackout"),
path('contact/',views.contact,name="contact"),
path('shop_detail/',views.shop_detail,name="shop_detail"),
path('get_seller_products/',views.get_seller_products,name="get_seller_products"),
path('search/', views.search, name="search"),
path('logout/',views.logout,name="logout"),
path('product_list/',views.product_list,name="product_list"),
path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
path('cart_count/', views.cart_count, name='cart_count'),
path('delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
path('update_total_price/', views.update_total_price, name='update_total_price'),
path('update_cart_item_quantity/', views.update_cart_item_quantity, name='update_cart_item_quantity'),
path('add_product/',views.add_product,name="add_product"),
path('checkout/',views.checkout,name="checkout"),
path('submit_order/',views.submit_order,name="submit_order"),
path('get_seller_productsd/',views.get_seller_productsd,name="get_seller_productsd"),
path('delete_product/',views.delete_product,name="delete_product"),







]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)