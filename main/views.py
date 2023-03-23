


from django.shortcuts import  render,redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


@login_required(login_url='http://127.0.0.1:8000/')
def main(request):
    return render(request,"main.html")



@login_required(login_url='http://127.0.0.1:8000/')
def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'profile.html', {'file_url': file_url})
    return render(request, 'upload.html')
    







