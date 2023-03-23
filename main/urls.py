from django.urls import include , path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.main, name='main'),
   path('compete/', include('compete.urls')),
   path('upload/', views.upload, name='upload'),
   path('interact/', include('interact.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)