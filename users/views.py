from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

@login_required
def index(request):
    return render(request,'expense/index.html')
def sign_up(request):
    context = {}
    form =  UserRegisterForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            user = form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Acount was created for ' + user)
            #login(request,user)
            return redirect('login')
    context['form']=form
    return render(request,'registration/sign_up.html',{'form':form})

def loginPage(request):
    context={}
    return redirect(request,'registration/login.html')


def logout(request):
    context={}
    return redirect(request,'users/logged_out.html')
