from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def log(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        data=authenticate(username=username,password=password)
        if data:
            login(req,data)
            return redirect(admin_home)
        else:
            return redirect(log)
    else:
        messages.warning(req, " Invalid username and password.")
        return render(req,'login.html')
    
# admin home 
    
def admin_home(req):
    return render(req,'admin/home.html')

# registration page

def reg(req):
    return render(req,'register.html')

