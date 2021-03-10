from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Prisoner
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')


def logout_user(request):
    logout(request)
    return redirect('home')

def login_user(request):
    if request.user.is_authenticated:
        logout(request)

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username , password = password)
            print(user)
            if user is not None:
                print(user.first_name)
                if user.first_name == request.POST.get('post') == "Admin":
                    print(user.first_name)
                    login(request, user)
                    return redirect('admin_after_login')

                if user.first_name == request.POST.get('post') == "Jailor":
                    login(request, user)
                    print(user.first_name)
                    return redirect('jailor_after_login')

                if user.first_name == request.POST.get('post') == "Lawyer":
                    print(user.first_name)
                    login(request, user)
                    return redirect('lawyer_after_login')

            else:
                messages.info(request,'Username or Password is incorrect')

    return render(request,'login_page.html')



def admin_after_login(request):
    return render(request,'admin_after_login.html')

def jailor_after_login(request):
    return render(request,'jailor_after_login.html')

def lawyer_after_login(request):
    return render(request,'lawyer_after_login.html')


def viewprisoner(request):
    if request.method == "POST" :
        list = request.POST.get('id').split(' ')
        id = list[-1]
        return redirect('prisonerinfo',id)
    prisoners = Prisoner.objects.all()
    context = { "data" : prisoners }
    return render(request,'viewprisoner.html' , context)

def addprisoner(request):
    if request.method == 'POST':
        prisoner = Prisoner()
        prisoner.pic = request.FILES['prisoner_img']
        prisoner.name = request.POST.get('fullname')
        prisoner.age = request.POST.get('age')
        prisoner.gender = request.POST.get('gender')
        prisoner.state = request.POST.get('state')
        prisoner.address = request.POST.get('address')
        prisoner.case = request.POST.get('case')
        prisoner.parole = request.POST.get('parole')
        prisoner.save()

    return render(request,'addprisoner.html')


def addjailor(request):
    form = CreateUserForm()

    if request.method == 'POST' :
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account created for " + user)
            user = User.objects.get(username = user)
            user.first_name = "Jailor"
            user.save()

    context = {'form':form}
    return render(request,'addjailor.html',context)



def addlawyer(request):
    form = CreateUserForm()

    if request.method == 'POST' :
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account created for " + user)
            user = User.objects.get(username = user)
            user.first_name = "Lawyer"
            user.save()

    context = {'form':form}
    return render(request,'addlawyer.html',context)


def viewjailor(request):
    jailors = User.objects.filter(first_name = "Jailor")
    context = {"Jailors" : jailors}
    return render(request,'viewjailor.html',context)

def viewlawyer(request):
    lawyers = User.objects.filter(first_name = "Lawyer")
    print(lawyers)
    context = {"Lawyers" : lawyers}
    return render(request,'viewlawyer.html',context)


def jailorinfo(request):
    return render(request,'jailorinfo.html')

def prisonerinfo(request,id):
    p = Prisoner.objects.get(id=id)
    print(p)
    context = {"prisoner" : p}
    print(p.id,p.name,p.age)
    return render(request,'prisonerinfo.html',context)
