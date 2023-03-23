from django.urls import include , path
from . import views

urlpatterns = [
   path('', views.interact, name='interact'),
   path('secondpage1/', views.secondpage1, name='secondpage1'),
   path('Team/', views.team, name='team'),
   path('Teammates/', views.teammates, name='teammates'),

]