from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register, name="register"),
    path("mainpage/",include('main.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)