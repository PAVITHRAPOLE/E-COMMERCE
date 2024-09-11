from django.shortcuts import render,redirect
from .models import Register
def index(request):
    return render(request,'index.html')

def viewusers(request):
    #all() methods returns all rows as Register class objects
    users=Register.objects.all()
    return render(request,'viewusers.html',{"users":users})

def modify(request):
    operation=request.GET['operation']
    print(operation)
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    mobile=request.GET['mobile']
    address=request.GET['address']
    desig=request.GET['desig']
    r=Register.objects.get(email=email)
    if operation=="update":
        r.fullname=fullname
        r.email=email
        r.password=password
        r.mobile=mobile
        r.address=address
        r.desig=desig
        r.save()
    else:
        Register.delete(r)
    return render(request,"viewusers.html",{"users":Register.objects.all()})

def about(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def userhome(request):
    return render(request,'userhome.html')

def adminhome(request):
    return render(request,'adminhome.html')

def contact(request):
    return render(request,'contact.html')

def doregister(request):
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    mobile=request.GET['mobile']
    address=request.GET['address']
    country=request.GET['country']
    r=Register()
    r.name=fullname
    r.email=email
    r.password=password
    r.mobile=mobile
    r.address=address
    r.country=country
    r.save()
    return render(request,'login.html',{"msg":"Registration successful"})

def logincheck(request):
    email=request.GET['email']
    password=request.GET['password']
    r=None
    try:
        r=Register.objects.get(email=email,password=password)
        print("r=",r)
    except Exception as ex:
       return render(request,'login.html',{"msg":"Invalid Emailid\password"})
    if(r!=None):
        if(r.desig=='user'):
            return redirect('/userhome')
        if(r.desig=='admin'):
            return redirect('/adminhome')
        else:
            return render(request,"login.html",{"msg":"Invalid Designation"})

def amazon(request):
    return render(request,'amazon.html')

def fashion(request):
    return render(request,'fashion.html')

def success(request):
    return render(request,'success.html')