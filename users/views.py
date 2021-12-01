from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Profile, Skill

# Create your views here.

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'User name or password is incorrect')

    return render(request, 'users/login-register.html', {'page':page})


def logoutUser(request):
    logout(request)
    messages.info(request,'User is logged out')
    return redirect('login')
    

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form  = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Yay! you have successfully registered!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Oops! Something went wrong!')

    context = {'page':page, "form":form}
    return render(request, 'users/login-register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    skillset = profile.skill_set.exclude(description='')
    otherskill = profile.skill_set.filter(description='')
    context = {'profile':profile, 'skillset':skillset, 'otherskill':otherskill}
    return render(request, 'users/user-profile.html', context)