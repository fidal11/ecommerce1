from django.db import models
from ecommerce_app.models import Seller1
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=30)  
    seller = models.ForeignKey(Seller1, on_delete = models.CASCADE) 
    description=models.CharField(max_length = 100)
    stock=models.IntegerField()
    code=models.CharField(max_length=20)
    price=models.FloatField()
    image = models.ImageField(upload_to  = 'product/')

    class Meta:
        db_table = 'product_tb'



