from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prize(models.Model):
    pass

class Achievement(models.Model):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to='profile_images', blank=True)
    currency = models.IntegerField(default=100)

    prizes = models.ManyToManyField(Prize)
    achievements = models.ManyToManyField(Achievement)




