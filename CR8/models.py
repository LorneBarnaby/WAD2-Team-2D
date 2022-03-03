from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prize(models.Model):

    prizeName = models.CharField(max_length=30)
    prizeImage = models.ImageField(upload_to='prize_images')
    prizeValue = models.IntegerField(default=0)
    prizeRarity = models.CharField(max_length=30)


class Achievement(models.Model):

    achievementName = models.CharField(max_length=30)
    achievementDescription = models.CharField(max_length=256)
    achievementImage = models.ImageField(upload_to='achievement_images')


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





