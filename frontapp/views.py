from django.shortcuts import render,redirect
from shopapp.models import CategoryDB,productDB,itemDB,generesdb
from frontapp.models import customerdetails,newcartdb,checkoutdb
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db.models import Sum




# Create your views here.
def home(request):
    data=CategoryDB.objects.all()
    tata=generesdb.objects.all()
    ctgry=CategoryDB.objects.all()
    messages.success(request, "Product added successfully")
    return render(request,"1homepage.html",{'data':data,"tata":tata,'ctgry':ctgry})
def product(request,itemcat):
    products=productDB.objects.filter(Categoryname=itemcat)
    data=CategoryDB.objects.all()
    tata=productDB.objects.all()
    return render(request,"2productpage.html",{'products':products,"data":data,"tata":tata})

def typess(req,itemcat):
    brand=productDB.objects.filter(Type=itemcat)
    tata=productDB.objects.all()
    data=CategoryDB.objects.all()
    return render(req,"3type.html",{"brand":brand,'tata':tata,"data":data})

def single(request,dataid):
    productss=itemDB.objects.get(id=dataid)
    data=CategoryDB.objects.all()
    return render(request,"4single.html",{"productss":productss,'data':data})

def items(req,itemcat):
    products=itemDB.objects.filter(productname=itemcat)
    data=itemDB.objects.all()
    ctgry = CategoryDB.objects.all()
    return render(req,"items01.html",{'products':products,"data":data,'ctgry':ctgry})

def cart(req):
    data = CategoryDB.objects.all()
    # newproducts = itemDB.objects.get(id=dataid)
    cart=newcartdb.objects.filter(userr=req.session['username'])
    cart_session=newcartdb.objects.filter(userr=req.session['username'])
    grandtotal=cart.aggregate(Sum("totalprices"))["totalprices__sum"]
    return render(req,"5cart.html",{"data":data,"cart":cart,"cart_session":cart_session,"grandtotal":grandtotal})

def savecartt(request):
    if request.method=="POST":

        nm=request.POST.get('name')
        pr=request.POST.get('price')
        qt=request.POST.get('quantity')
        ss=request.POST.get('size')
        tl=request.POST.get('tp')
        ur=request.POST.get('user')
        product_id = request.POST.get('productimagee')
        pimage = itemDB.objects.get(id=product_id)
        image = pimage.Imagee
        obj=newcartdb(names=nm,prices=pr,quantities=qt,sizes=ss,totalprices=tl,userr=ur,Imagee=image)
        obj.save()
        return redirect(home)

def deletecart(request, dataid):
    data=newcartdb.objects.filter(id=dataid)
    data.delete()
    messages.warning(request,"Product Removed From Cart")
    return redirect(cart)

def about(request):
    data = CategoryDB.objects.all()
    return render(request,"about02.html",{"data":data})

def contact(request):
    messages.success(request,"Message sent successfully")
    return render(request,"7contactpage.html")

def checkout(req):
    cart = newcartdb.objects.filter(userr=req.session['username'])
    grandtotal = cart.aggregate(Sum("totalprices"))["totalprices__sum"]
    return render(req,"8checkoutpage.html",{"cart":cart,"grandtotal":grandtotal})

def userlogin(request):
    return render(request,"6userlogin.html")

def usersavedata(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        passw = req.POST.get('password')
        cpassw = req.POST.get('confirmpassword')
        obj = customerdetails(Username=na,Email=em,Password=passw,Confirmpassword=cpassw)
        obj.save()
        return redirect(userlogin)

def userloginpage(request):
    if request.method=="POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if customerdetails.objects.filter(Username=username_r,Password=password_r).exists():
            data=customerdetails.objects.filter(Username=username_r,Password=password_r).values('Email','id').first()

            request.session['username']=username_r
            request.session['password']=password_r
            return redirect(home)
        else:
            return redirect(userlogin)
    else:
        return redirect(userlogin)

def profile(req):
    return render(req,"profilepage.html")

def userlogout(request):
    if request.session:
        request.session.clear()
    return redirect(userlogin)

def savecheckout(req):
    if req.method=="POST":

        fm=req.POST.get('fname')
        lm=req.POST.get('lname')
        ctry=req.POST.get('country')
        add=req.POST.get('address')
        tc=req.POST.get('towncity')
        pin=req.POST.get('pincode')
        ph=req.POST.get('phone')
        em=req.POST.get('emailaddress')
        obj=checkoutdb(Fname=fm,Lname=lm,Country=ctry,Address=add,Towncity=tc,Pincode=pin,Phone=ph,Emailaddress=em)
        obj.save()
        messages.success(req, "product saved successfully")
        return redirect(checkout)

def allpro(req):
    data = itemDB.objects.all()
    bata = CategoryDB.objects.all()
    return render(req,"allproducts.html",{"data":data,"bata":bata})

