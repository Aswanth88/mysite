from dis import get_instructions
from msilib.schema import ListView
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
import tkinter
from tkinter import messagebox
from django.contrib import auth

def index(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("mainpage/")
		          
			     
			else:
				messages.error(request,"Invalid username or password.")
				messagebox.showinfo("Unsuccessful login", "Invalid information")
		else:
			messages.error(request,"Invalid username or password.")
			messagebox.showinfo("Unsuccessful login", "Invalid information")
	form = AuthenticationForm()
	return render(request=request, template_name="auth.html", context={"login_form":form})


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request,"Registration successful." )
			messagebox.showinfo("success", "Registration successful")
			return redirect("http://127.0.0.1:8000")
		messages.error(request, "Unsuccessful registration. Invalid information.")
		messagebox.showinfo("Unsuccessful registration", "Invalid information")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"form":form})





	
