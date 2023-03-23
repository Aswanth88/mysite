
from django.urls import include , path
from . import views

urlpatterns = [
   path('', views.VS, name='VS'),
   path('positiveside/', views.index, name='positive'),
    path('negativeside/', views.index1, name='negative'),
    path('view/', views.show_file, name="view"),
    path('view1/', views.show_file1, name="view1"),
   
    
]