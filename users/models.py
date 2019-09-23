from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=100, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)



    def __str__(self):

        return self.email





# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.

# class CustomUser(AbstractUser):

#     email = models.EmailField(max_length=200)

#     # name = models.CharField(max_length=200)



#     def __str__(self):

#         return self.email