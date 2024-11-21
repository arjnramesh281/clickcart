from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def log(req):
    if 'admin' in req.session:
        return redirect(admin_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        data=authenticate(username=username,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['admin']=username
                return redirect(admin_home)
            else:
                req.session['user']=username
                return redirect(user_home)
        else:
            messages.warning(req, " Invalid username or password.")
            return redirect(log)
    else:
        return render(req,'login.html')

# admin logout

def admin_logout(req):
    logout(req)
    req.session.flush()
    return redirect(log)

# admin home 
    
def admin_home(req):
    if 'admin' in req.session:
        data=Product.objects.all()
        return render(req,'admin/home.html',{'products':data})
    else:
        return redirect(log)


# add product

def add_pro(req):
    if 'admin' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            dis=req.POST['dis']
            price=req.POST['price']
            off_price=req.POST['off_price']
            stock=req.POST['stock']
            file=req.FILES['img']
            data=Product.objects.create(pid=pid,name=name,dis=dis,price=price,off_price=off_price,stock=stock,img=file)
            data.save()
            return redirect(admin_home)
        else:
            return render(req,'admin/add_pro.html')
    else:
        return redirect(log)



# registration page

def reg(req):
    if req.method=='POST':
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=username,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req, " This Email Already In Use.")
            return redirect(reg)
        return redirect(log)
    else:
     return render(req,'user/register.html')

def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,"user/home.html",{"products":data})
    else:
        return redirect(log)


def view_product(req,pid):
    data= Product.objects.get(pk=pid)
    return render(req,'user/viewpro.html',{'product': data})


def add_to_cart(req,pid):
    product=Product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.create(product=product,user=user,qty=1)
    data.save()
    return redirect(view_cart)

def view_cart(req):
    return render(req,'user/cart.html')