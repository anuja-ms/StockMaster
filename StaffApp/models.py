from django.db import models

from AdminApp.models import Tbl_dealer, Tbl_product, Tbl_staff


# Create your models here.
class Tbl_requestmaster(models.Model):
    requestmasterid = models.AutoField(primary_key=True)
    deliverydate = models.DateField(null=True)
    totalamount = models.IntegerField()
    status = models.CharField(max_length=25)
    dealerid = models.ForeignKey(Tbl_dealer, on_delete=models.CASCADE, null=True)

class Tbl_requestdetails(models.Model):
    requestid = models.AutoField(primary_key=True)
    productid = models.ForeignKey(Tbl_product,on_delete=models.CASCADE)
    staffid = models.ForeignKey(Tbl_staff,on_delete=models.CASCADE)
    requestdate = models.DateField()
    remark = models.CharField(max_length=25,null=True)
    price = models.IntegerField(null=True)
    status = models.CharField(max_length=25)
    quantity = models.IntegerField(null=True)
    requestmasterid = models.ForeignKey(Tbl_requestmaster,on_delete=models.CASCADE,null=True)
    dealerquantity=models.IntegerField(null=True)

class Tbl_salesmaster(models.Model):
    salesmasterid = models.AutoField(primary_key=True)
    salesdate = models.DateField()
    totalamount = models.IntegerField()
    billingno = models.IntegerField()

class Tbl_salesdetails(models.Model):
    salesdetailsid = models.AutoField(primary_key=True)
    salesmasterid = models.ForeignKey(Tbl_salesmaster,on_delete=models.CASCADE,null=True)
    productid = models.ForeignKey(Tbl_product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    productamount = models.IntegerField()
    staffid= models.ForeignKey(Tbl_staff,on_delete=models.CASCADE,null=True)

class Tbl_purchasemaster(models.Model):
    purchasemasterid = models.AutoField(primary_key=True)
    purchasedate = models.DateField()
    dealerid = models.ForeignKey(Tbl_dealer,on_delete=models.CASCADE)
    totalamount = models.IntegerField()
    billno = models.IntegerField()

class Tbl_purchasedetails(models.Model):
    purchasedetailsid = models.AutoField(primary_key=True)
    purchasemasterid = models.ForeignKey(Tbl_purchasemaster,on_delete=models.CASCADE,null=True)
    productid = models.ForeignKey(Tbl_product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    productprice = models.IntegerField()
    staffid= models.ForeignKey(Tbl_staff,on_delete=models.CASCADE,null=True)

class Tbl_payment(models.Model):
    paymentid =  models.AutoField(primary_key=True)
    purchasemasterid = models.ForeignKey(Tbl_purchasemaster,on_delete=models.CASCADE)
    Amount = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=25)