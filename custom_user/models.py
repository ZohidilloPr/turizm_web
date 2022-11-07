from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    profile_img = models.ImageField(default='media/default/default.png', upload_to='profile_images/')
