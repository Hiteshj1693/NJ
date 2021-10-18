from django.shortcuts import redirect, render
from .forms import SignupForm
from .models import SignupMaster
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=="POST":
        unm=request.POST['username']
        pas=request.POST['password']

        user=SignupMaster.objects.filter(username=unm,password=pas)
        if user:
            print("Signup successfully!")
            request.session['user']=unm
            return redirect('home')
        else:
            print("Login Failed!")
    else:
        print("Something Went Wrong!")
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        signupfrm=SignupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm.save()
            print("Signup Successgfully!")
            return redirect('home')
        else:
            print(signupfrm.errors)
    else:
        signupfrm=SignupForm()
    return render(request,'signup.html')

def home(request):
    #user=request.session.get('user')
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect("/")