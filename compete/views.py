from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='http://127.0.0.1:8000/')
def compete(request):
    return render(request,"compete.html")


@login_required(login_url='http://127.0.0.1:8000/')
def secondpage(request):
    return render(request,"secondpage.html")
