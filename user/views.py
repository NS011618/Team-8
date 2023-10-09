from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from user.models import course
from user import forms
# Create your views here.
def home(request):
    return render(request,'user/index.html')


def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"User Created Successfully")
        return redirect('signin')
 
    return render(request,'user/signup.html')

def display(request):
    ec_list=course.objects.all()
    my_dict={'ec_list':ec_list}
    return render(request,'user/cdetails.html',context=my_dict)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password = pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return redirect('cdetail')
        else:
            messages.error(request,"Enter correct details")
            return redirect('home')
    return render(request,'user/signin.html')


def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')



def cinpt(request):    
    form=forms.ceform()
    if request.method=='POST':
        form=forms.ceform(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('cdetail')
            
    return render(request,'user/courinpt.html',{'form':form})


def cartadd(request):
    ec_list=course.objects.all()
    my_dict={'ec_list':ec_list}
    return render(request,'user/cart.html',context=my_dict)  
