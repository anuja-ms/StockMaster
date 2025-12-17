from django.db import models

from GuestApp.models import Tbl_login


# Create your models here.
class Tbl_district(models.Model):
    districtid = models.AutoField(primary_key=True)
    districtname = models.CharField(max_length=25)

class Tbl_location(models.Model):
    locationid = models.AutoField(primary_key=True)
    locationname = models.CharField(max_length=25)
    districtid = models.ForeignKey(Tbl_district,on_delete=models.CASCADE)

class Tbl_brand(models.Model):
    brandid = models.AutoField(primary_key=True)
    brandname = models.CharField(max_length=25)
    brandimage = models.ImageField()

class Tbl_category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=25)
    categoryimage = models.ImageField()

class Tbl_subcategory(models.Model):
    subcategoryid = models.AutoField(primary_key=True)
    subcategoryname = models.CharField(max_length=25)
    image = models.ImageField()
    categoryid = models.ForeignKey(Tbl_category,on_delete=models.CASCADE)

class Tbl_dealer(models.Model):
    dealerid = models.AutoField(primary_key=True)
    dealername = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    contactno=models.BigIntegerField()
    locationid = models.ForeignKey(Tbl_location,on_delete=models.CASCADE)
    loginid = models.ForeignKey(Tbl_login,on_delete=models.CASCADE)

class Tbl_staff(models.Model):
    staffid = models.AutoField(primary_key=True)
    staffname = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    contactno=models.BigIntegerField()
    locationid = models.ForeignKey(Tbl_location,on_delete=models.CASCADE)
    loginid = models.ForeignKey(Tbl_login,on_delete=models.CASCADE)
    categoryid = models.ForeignKey(Tbl_category,on_delete=models.CASCADE,null=True,blank=True)

class Tbl_product(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    price=models.BigIntegerField()
    unit=models.CharField(max_length=25)
    image = models.ImageField()
    dealerprice=models.IntegerField(default=0)
    subcategoryid = models.ForeignKey(Tbl_subcategory,on_delete=models.CASCADE)
    brandid = models.ForeignKey(Tbl_brand,on_delete=models.CASCADE)

class Tbl_stock(models.Model):
    stockid = models.AutoField(primary_key=True)
    productid = models.ForeignKey(Tbl_product,on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    Reorderlevel = models.IntegerField(default=0)