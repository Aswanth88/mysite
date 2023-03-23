from django.shortcuts import  render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, HttpResponse

from .forms import MyfileUploadForm, MyfileUploadForm1
from .models import file_upload , file_upload1
from tkinter import messagebox


@login_required(login_url='http://127.0.0.1:8000/')
def VS(request):
    return render(request,"VS.html")



@login_required(login_url='http://127.0.0.1:8000/')
def index(request):



    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)


        print(form.as_p)
        
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']
           
    
            file_upload(file_name=name, my_file=the_files).save()
            
          
            messagebox.showinfo("successful Submission", "You can now see other opinions")
            return redirect("http://127.0.0.1:8000/mainpage/compete/VS/view/")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':MyfileUploadForm()
        }      
        
        return render(request, 'positive.html', context)
        


@login_required(login_url='http://127.0.0.1:8000/')
def show_file(request):
    # this for testing 
    all_data = file_upload.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'view.html', context)




@login_required(login_url='http://127.0.0.1:8000/')
def index1(request):



    if request.method == 'POST':
        form = MyfileUploadForm1(request.POST, request.FILES)


        print(form.as_p)
        
        if form.is_valid():
            name = form.cleaned_data['file_names']
            the_files = form.cleaned_data['files_datas']
           
    
            file_upload1(file_names=name, my_file1=the_files).save()
            
          
            messagebox.showinfo("successful Submission", "You can now see other opinions")
            return redirect("http://127.0.0.1:8000/mainpage/compete/VS/view1/")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':MyfileUploadForm1()
        }      
        
        return render(request, 'negative.html', context)
        

@login_required(login_url='http://127.0.0.1:8000/')
def show_file1(request):
    # this for testing 
    all_data1 = file_upload1.objects.all()

    context = {
        'data':all_data1
        }

    return render(request, 'view1.html', context)


