from django.shortcuts import render,redirect
from django.http import HttpResponse
from shopapp.models import CategoryDB,productDB,itemDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
def homepage1(request):
    return render(request,"homepage.html")

def categorypage(request):
    return render(request,"category.html")

def savecategory(req):
    if req.method=="POST":
        cna = req.POST.get('categoryname')
        des = req.POST.get('description')
        img = req.FILES['image']

        obj = CategoryDB(Categoryname=cna,Description=des,Image=img)
        obj.save()
        messages.success(req, "category saved successfully")
        return redirect(categorypage)

def categorydisplay(request):
    data = CategoryDB.objects.all()
    return render(request,"categorydisplay.html", {'data':data})

def editcategory(req,dataid):
    data = CategoryDB.objects.get(id=dataid)
    print(data)
    return render(req,"editcategory.html",{'data':data})

def updatecategory(req,dataid):
    if req.method == "POST":
        cna = req.POST.get('categoryname')
        des = req.POST.get('description')
        img = req.FILES['image']
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Image
        CategoryDB.objects.filter(id=dataid).update(Categoryname=cna,Description=des,Image=img)
        return redirect(categorydisplay)

def categorydelete(request,dataid):
    data=CategoryDB.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "Category Deleted")
    return redirect(categorydisplay)

def addproductpage(request):
    data=CategoryDB.objects.all()
    product=productDB.objects.all()
    return render(request,"Addproduct.html",{"data":data,"product":product})
def saveproduct(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ca = request.POST.get('categoryname')
        pr=request.POST.get('price')
        sz=request.POST.get('size')
        col=request.POST.get('color')
        tp=request.POST.get('type')
        abt=request.POST.get('about')
        img=request.FILES['image']
        obj=productDB(Name=na,Categoryname=ca,Price=pr,Size=sz,Color=col,Type=tp,About=abt,Image=img)
        obj.save()
        messages.success(request, "Product added successfully")

        return redirect(addproductpage)

def displayproduct(request):
    data=productDB.objects.all()
    return render(request,"Displayproduct.html",{'data':data})
def editproduct(req,dataid):
    data=productDB.objects.get(id=dataid)
    bata=CategoryDB.objects.all()
    print(data)
    return render(req,"Editproduct.html",{'data':data,"bata":bata})

def updateproduct(req,dataid):
    if req.method=="POST":
        na=req.POST.get('name')
        ca=req.POST.get('category')
        pr=req.POST.get('price')
        sz=req.POST.get('size')
        col=req.POST.get('color')
        gt=req.POST.get('genrstype')
        abt=req.POST.get('about')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=productDB.objects.get(id=dataid).Image
        productDB.objects.filter(id=dataid).update(Name=na,Categoryname=ca,Price=pr,Size=sz,Color=col,Type=gt,About=abt,Image=img)
        return redirect(displayproduct)

def deleteproduct(request, dataid):
    data=productDB.objects.filter(id=dataid)
    data.delete()
    messages.error(request,"Product Deleted Successfully")
    return redirect(displayproduct)

def loginpage(request):
    return render(request,"adminlogin.html")
def adminlogin(req):
    if req.method=="POST":
        username_r=req.POST.get('username')
        password_r=req.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(homepage1)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def additems(req):
    data=CategoryDB.objects.all()
    tata=productDB.objects.all()
    return render(req,"additems01.html",{"data":data,"tata":tata})
def saveitems(req):
    if req.method=="POST":
        na=req.POST.get('name')
        ca = req.POST.get('categoryname')
        pn = req.POST.get('productname')
        pr=req.POST.get('price')
        sz=req.POST.get('size')
        col=req.POST.get('color')
        tp=req.POST.get('type')
        abt=req.POST.get('about')
        img=req.FILES['image']
        obj=itemDB(Namee=na,Categorynamee=ca,productname=pn,Pricee=pr,Sizee=sz,Colorr=col,Typee=tp,Aboutt=abt,Imagee=img)
        obj.save()
        messages.success(req, "Item added successfully")
        return redirect(additems)
def displayitems(request):
    data=itemDB.objects.all()
    return render(request,"01displayitems.html",{'data':data})
def edititems(req,dataid):
    data=itemDB.objects.get(id=dataid)
    bata=CategoryDB.objects.all()
    sata=productDB.objects.all()
    print(data)
    return render(req,"02edititems.html",{'data':data,"bata":bata,'sata':sata})

def updateitem(req,dataid):
    if req.method=="POST":
        na=req.POST.get('name')
        ca=req.POST.get('category')
        pr=req.POST.get('price')
        sz=req.POST.get('size')
        col=req.POST.get('color')
        gt=req.POST.get('genretype')
        abt=req.POST.get('about')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=itemDB.objects.get(id=dataid).Image
        itemDB.objects.filter(id=dataid).update(Namee=na,Categorynamee=ca,Pricee=pr,Sizee=sz,Colorr=col,Typee=gt,Aboutt=abt,Imagee=img)
        return redirect(displayitems)
def deleteitem(request, dataid):
    data=itemDB.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "Item Deleted Successfully")
    return redirect(displayitems)

