from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static

class User(AbstractUser):
    photo = models.ImageField(upload_to='images/')

class Raqam(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name