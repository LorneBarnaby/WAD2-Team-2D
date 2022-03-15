from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from CR8.rarity import RARITY


class Prize(models.Model):
    prizeName = models.CharField(max_length=30, blank=True, unique=True)
    prizeImage = models.ImageField(upload_to="prize_images", blank=True)
    prizeValue = models.IntegerField(default=0)
    prizeRarity = models.CharField(max_length=30, blank=True, choices=RARITY.model_choices())

    def __str__(self):
        return self.prizeName


class Achievement(models.Model):
    achievementName = models.CharField(max_length=30, blank=True)
    achievementDescription = models.CharField(max_length=256, blank=True)
    achievementImage = models.ImageField(upload_to="achievement_images", blank=True)

    # Commented out until population script is updated to populate these fields
    #achievementType = models.CharField(max_length=10)
    #achievementCriteriaExpectedVal = models.IntegerField(default=0)

    def __str__(self):
        return self.achievementName


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(
        upload_to="profile_images", blank=True, default="profile_images/none.jpg"
    )
    currency = models.IntegerField(default=100)

    prizes = models.ManyToManyField(Prize, blank=True)
    achievements = models.ManyToManyField(Achievement, blank=True)

    username_slug = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.username_slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)
