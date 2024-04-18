from django.db import models

# Create your models here.


from django.db import models

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # Add other fields as needed

    def __str__(self):
        return self.name
    
class buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # Add other fields as needed

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    # Add other fields as needed

    def __str__(self):
        return self.name

class products1(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.FileField(upload_to='media/', null=True, blank=True) 
    # Add other fields as needed

    def __str__(self):
        return self.name