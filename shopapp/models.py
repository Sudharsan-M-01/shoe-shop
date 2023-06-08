from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Categoryname = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="profile",null=True,blank=True)

class productDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Categoryname = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=100, null=True, blank=True)
    Size = models.CharField(max_length=100, null=True, blank=True)
    Color = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=100, null=True, blank=True)
    About = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)


class itemDB(models.Model):
    Namee = models.CharField(max_length=100, null=True, blank=True)
    Categorynamee = models.CharField(max_length=100, null=True, blank=True)
    productname = models.CharField(max_length=100, null=True, blank=True)
    Pricee = models.CharField(max_length=100, null=True, blank=True)
    Sizee = models.CharField(max_length=100, null=True, blank=True)
    Colorr = models.CharField(max_length=100, null=True, blank=True)
    Typee = models.CharField(max_length=100, null=True, blank=True)
    Aboutt = models.CharField(max_length=100, null=True, blank=True)
    Imagee = models.ImageField(upload_to="profile", null=True, blank=True)

class generesdb(models.Model):
    Generess = models.CharField(max_length=100, null=True, blank=True)

