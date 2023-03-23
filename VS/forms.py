from django import forms

class MyfileUploadForm(forms.Form):

    file_name =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    files_data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

class MyfileUploadForm1(forms.Form):   
    file_names =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    files_datas = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))