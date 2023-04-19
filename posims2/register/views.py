from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def register(response):
    if response.method=="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save() 
            messages.info(response, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(response, new_user)
            return redirect("home")
            
    else:
        form = RegisterForm()

    context={"form":form}
    return render(response,"register/register.html",context)
