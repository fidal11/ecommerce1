from django.db import models

# Create your models here.
class Seller1(models.Model):
    sellername=models.CharField(max_length=100)
    mobileno=models.BigIntegerField()
    email=models.CharField(max_length=100)
    companyname=models.CharField( max_length=100)
    password=models.CharField(max_length=100,default='')
    username=models.IntegerField(default=1)
    ac_holder_name = models.CharField(max_length = 30 ,default = '')
    ifsc = models.CharField(max_length = 20, default = '')
    branch= models.CharField(max_length = 30, default = '')
    ac_no = models.CharField(max_length = 30, default = '')
    image = models.ImageField(upload_to  = 'seller/')
    gender = models.CharField(max_length = 30,default='')

    class Meta:
            db_table = 'seller_tb'


class Customer(models.Model):
    customername=models.CharField(max_length=100)
    customermobile=models.BigIntegerField()
    customermail=models.CharField(max_length=100)
    customerpassword=models.CharField(max_length=100,default='')

    class Meta:
        db_table = 'customer_tb'

