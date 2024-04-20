from django.contrib import admin

# Register your models here.

from .models import*

admin.site.register(products1)
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(buyer)
admin.site.register(CartItem)



