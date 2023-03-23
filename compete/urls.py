from django.urls import include , path
from . import views

urlpatterns = [
   path('', views.compete, name='compete'),
   path('secondpage/', views.secondpage, name='secondpage'),
   path('VS/', include('VS.urls')),

]