from django.db import models

# Create your models here.
class customerdetails(models.Model):
    Username = models.CharField(max_length=30, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=100,null=True, blank=True)
    Confirmpassword = models.CharField(max_length=100,null=True, blank=True)

class newcartdb(models.Model):
    names = models.CharField(max_length=100,null=True,blank=True)
    prices = models.IntegerField(max_length=100,null=True,blank=True)
    quantities = models.IntegerField(max_length=100,null=True,blank=True)
    sizes = models.CharField(max_length=100,null=True,blank=True)
    totalprices = models.IntegerField(max_length=100,null=True,blank=True)
    userr = models.CharField(max_length=100,null=True,blank=True)
    Imagee=models.ImageField(upload_to="profile",null=True,blank=True)

class checkoutdb(models.Model):
    Fname = models.CharField(max_length=100, null=True, blank=True)
    Lname = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Towncity = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(max_length=100, null=True, blank=True)
    Emailaddress = models.EmailField(max_length=100, null=True, blank=True)