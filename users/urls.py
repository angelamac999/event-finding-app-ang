from django.urls import path, include
from django.conf.urls import include, url
from . import views



app_name = 'users'

urlpatterns = [
    path('event-finder/', include('eventFinderApp.urls')),
    path('register/', views.Register.as_view(), name='register'),
    path('users/', include('django.contrib.auth.urls')),
   ]