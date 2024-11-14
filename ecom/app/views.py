from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def log(req):
    if 'admin' in req.session:
        return redirect(admin_home)
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        data=authenticate(username=username,password=password)
        if data:
            login(req,data)
            req.session['admin']=username
            return redirect(admin_home)
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
        return render(req,'admin/home.html')
    else:
        return redirect(log)

# registration page

def reg(req):
    return render(req,'register.html')

