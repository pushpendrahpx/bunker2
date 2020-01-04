from django.urls import path
from . import views
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('upload/', views.upload, name='upload'),  
    path('reg/', views.mlr, name='mlr'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    