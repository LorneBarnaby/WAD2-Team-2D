from population_data_and_methods import (
    generate_user_lists,
    generate_prize_lists,
    generate_achievement_lists,
)
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cr8_project.settings")
import django

django.setup()
from CR8.models import UserProfile, Prize, Achievement
from django.contrib.auth.models import User
from django.core.files import File


def populate():
    prize_list = generate_prize_lists()
    user_list = generate_user_lists()
    achievement_list = generate_achievement_lists()

    for user in user_list:
        add_user(user)

    for prize in prize_list:
        add_prize(prize)

    for achieve in achievement_list:
        add_achievement(achieve)

    image_check = input(
        """Please enter 'n' if you would like to skip adding images
    might be helpful if you've already done it as adding images
    once you've already added them makes loads of duplicate images"""
    )

    if image_check != "n" or image_check != "N":
        pass


def add_user(user):
    username = user["username"]
    u = User.objects.get_or_create(username=username)[0]
    u.set_password(user["password"])
    u.save()
    profile = UserProfile.objects.get_or_create(user=u)[0]
    profile.currency = user["currency"]
    profile.save()
    dir = os.path.join(os.getcwd(), "tmp/prof/" + "1.jpg")
    profile.profileImage.save(f"{username}.jpg", File(open(dir, "rb")))
    return profile


def add_prize(prize):
    prize_name = prize["name"]
    p = Prize.objects.get_or_create(prizeName=prize_name)[0]
    p.prizeValue = prize["value"]
    p.prizeRarity = prize["rarity"]
    p.save()
    dir = os.path.join(os.getcwd(), "tmp/prize/" + "1.png")
    p.prizeImage.save(f"{prize_name}.png", File(open(dir, "rb")))
    return p


def add_achievement(achieve):
    achievement_name = achieve["name"]
    a = Achievement.objects.get_or_create(achievementName=achievement_name)[0]
    a.achievementDescription = achieve["description"]
    a.save()
    dir = os.path.join(os.getcwd(), "tmp/achieve/" + "1.jpg")
    a.achievementImage.save(f"{achievement_name}.jpg", File(open(dir, "rb")))
    return a


populate()
