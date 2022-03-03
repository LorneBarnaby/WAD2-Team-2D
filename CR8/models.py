from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prize(models.Model):

    prizeName = models.CharField(max_length=30, blank=True, unique=True)
    prizeImage = models.ImageField(upload_to='prize_images', blank=True)
    prizeValue = models.IntegerField(default=0)
    prizeRarity = models.CharField(max_length=30, blank=True)


class Achievement(models.Model):

    achievementName = models.CharField(max_length=30, blank=True)
    achievementDescription = models.CharField(max_length=256, blank=True)
    achievementImage = models.ImageField(upload_to='achievement_images', blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to='profile_images', blank=True)
    currency = models.IntegerField(default=100)

    prizes = models.ManyToManyField(Prize)
    achievements = models.ManyToManyField(Achievement)
    website = models.URLField(blank=True)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username





