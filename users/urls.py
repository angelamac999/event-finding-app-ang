from django.urls import path, include
from django.conf.urls import include, url   
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView

# from django.contrib.auth import views as auth_views




urlpatterns = [

    path("register/", views.Register.as_view(), name="register"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    # url(r'^profile/edit/$', views.edit_profile, name = "edit_profile"),
    url(r'^profile/$', views.view_profile, name="view_profile"),
    # url(r'^change_password/$', views.change_password, name="change_password"),  
    # path('upload/', views.upload, name='upload'),
    path('pics/upload/', views.upload_pic, name="pic"),
    path("profile/password", views.change_password, name="edit password"),

]