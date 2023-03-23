from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required





@login_required(login_url='http://127.0.0.1:8000/')
def interact(request):
     return render(request,"interact.html")
    


@login_required(login_url='http://127.0.0.1:8000/')
def secondpage1(request):
    return render(request,"secondpage1.html")


@login_required(login_url='http://127.0.0.1:8000/')
def team(request):  
     return render(request,"team.html")


@login_required(login_url='http://127.0.0.1:8000/')
def teammates(request):  
     return render(request,"teammates.html")



