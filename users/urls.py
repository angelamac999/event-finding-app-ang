from django.urls import path, include
from django.conf.urls import include, url
from . import views


urlpatterns = [path("register/", views.Register.as_view(), name="register")]


# from django.urls import path, include
# from django.conf.urls import include, url
# from . import views



# app_name = 'users'

# urlpatterns = [
#     path('register/', views.Register.as_view(), name='register'),
# ]

