from django.db import models


class file_upload(models.Model):
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    my_file = models.FileField(upload_to='')
    
    def __str__(self):
        return self.file_name


class file_upload1(models.Model):
    ids = models.AutoField(primary_key=True)
    file_names = models.CharField(max_length=255)
    my_file1 = models.FileField(upload_to='')
    
    def __str__(self):
        return self.file_names