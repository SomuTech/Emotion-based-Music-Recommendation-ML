from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('',views.index,name='home')
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)