from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
      phone_number = models.CharField(max_length=255, blank=True,)


class Request(models.Model):

    CONTACT_METHOD = {
        "phone":"Phone",
        "email":"Email"
    }

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="images")
    contact_method = models.CharField(max_length=5, blank=False, choices=CONTACT_METHOD)