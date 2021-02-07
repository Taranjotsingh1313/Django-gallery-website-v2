from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from .models import image
# Create your views here.

# ***************DashBoard View******************
def imageshow(request):
        images = image.objects.all()
        return render(request,'index.html',{'images':images})

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
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')
# -----------add------
def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            imagetitle = request.POST['imagetitle']
            desc = request.POST['imagedesc']
            image2 = request.FILES['image1']
            if imagetitle  and desc and image2:
                image3 = image(img_title=imagetitle,img_desc=desc,image_file=image2,img_user=request.user)
                image3.save()
                messages.success(request,'Image Uploaded Successfully')
                return redirect('/add')
            else:
                return HttpResponse('No Fiels')
    else:
        return redirect('/')
    return render(request,'add.html',{})


# ----------Search View---------
def search(request):
    if request.user.is_authenticated:

        saerch = request.GET.get('search')
        print(saerch)
        img = image.objects.filter(img_title__icontains=saerch)
        imgdec = image.objects.filter(img_desc__icontains=saerch)
        # img1_user = image.objects.filter(image_user__icontains=saerch) 
        query = img.union(imgdec)
        context = {'query':query}
    else:
        return redirect('/')
    return render(request,'search.html',context)