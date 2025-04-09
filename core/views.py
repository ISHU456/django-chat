from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def frontpage (request):
    return render(request,'frontpage.html')

def signup(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request,"Password do not match")
            return redirect('signup')
        
        elif User.objects.filter(username = username).exists():
            messages.error(request,"username already exists")
            return redirect('signup')
        
        elif User is not None:
            my_auth = User.objects.create_user(username = username,email = email,password = password1)
            my_auth.save()
            login(request,my_auth)
            messages.success(request,"Account created successfully!")
            return redirect('home')
        
    return render(request,'signup.html')

def views_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid User")
    
    return render(request,'login.html')


def views_logout(request):
    logout(request)
    return redirect('signup')



@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'profile': profile, 'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    profile, created = Profile.objects.get_or_create(user=request.user) 
    return render(request,'user_list.html',{'users':users,'profile': profile})
