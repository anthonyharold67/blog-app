from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import UserForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST,request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile =form_profile.save(commit=False)#bilgileri al ama henüz database e  kaydetme çünkü userıda profile.usera tanımlama lazım
            profile.user = user
            profile.save()
            
            login(request,user)
            messages.success(request,"You have been registered")
            
            return redirect('home')
    context = {
        'form_user': form_user,
        'form_profile': form_profile
    }

    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()#formdan gelen bilgileri alıyoruz
        login(request, user)#formda gelen bilgilerle istek atıyoruz
        messages.success(request,"You have been logged in")
        return redirect('home')

    return render(request, 'users/login.html', {'form': form})    
    #contexti burada da oluşturabilirz

@login_required
def user_profile(request):
    user = User.objects.get(username=request.user)
    profile = UserProfile.objects.get(user=user)
    form_user = UserForm(instance=user)
    form_profile = UserProfileForm(instance=user.userprofile)
    if request.method == 'POST':
        form_user = UserForm(request.POST, instance=user)
        form_profile = UserProfileForm(request.POST, request.FILES,instance=user.userprofile)
        if form_user.is_valid():
            form_user.save()
            form_profile.save()
            login(request,user)
            messages.success(request,"You have been updated")   
            return redirect('home')
    context = {
        'form_user': form_user,
        'form_profile': form_profile,
        'profile': profile
    }
    return render(request, 'users/profile.html',context)


def user_logout(request):
    messages.success(request,"You have been logged out")
    logout(request)
    return render(request, 'users/logout.html') 