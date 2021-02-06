from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
# Create your views here.

# ***************DashBoard View******************
def imageshow(request):
    if not request.user.is_authenticated:
        # messages.error(request,'Please Login First')
        return redirect('login/')
    else:
        return render(request,'index.html',{})

# *****************Signing Up User***************
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            if data['name'] and data['email'] and data['password']:
                if data['password'] != data['password1']:
                    messages.error(request,'Password Donot Match')
                    return redirect(signup)
                if User.objects.filter(email=data['email']).first() or User.objects.filter(username=data['name']).first() or User.objects.filter(username=data['name'],email=data['email']).first() != None:
                    messages.error(request,'User Already Exist')
                    return redirect('/signup')
                else:
                    user = User.objects.create_user(username=data['name'],email=data['email'],password=data['password'])
                    user.save()
                    messages.success(request,'Your Account Has Been Created')
                    return redirect('/login')
            else:
                messages.error(request,'All Fields Required')
                return redirect('/signup')
    else:
        return redirect('/')
    return render(request,'contact.html')

# -------------------Login--------------------
def login1(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            if username and password:
                user = authenticate(request, username=username, password=password)
                print(user)
                if user:
                    login(request,user)
                    return redirect('/')
                elif user is None:
                    messages.error(request,"User Doesn't Exist")
                    return redirect('/login')
            else:
                messages.error(request,'All Fields Required')
                return render(request,'login.html')
    else:
        return redirect('/')
    return render(request,'login.html',{})

# ------------Logout----
def logout1(request):
    logout(request)
    return redirect('/')
