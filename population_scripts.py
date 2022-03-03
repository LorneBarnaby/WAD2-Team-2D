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


def populate():
    userIn = input(
        "If this is the first time this is run, enter 'y', otherwise enter anything else: "
    )
    prize_list = generate_prize_lists()
    user_list = generate_user_lists()
    achievement_list = generate_achievement_lists()
    if userIn == "y" or userIn == "Y":
        for user in user_list:
            add_user(user)

    for prize in prize_list:
        add_prize(prize)

    for achieve in achievement_list:
        add_achievement(achieve)


def add_user(user):
    u = User(username=user["username"])
    u.set_password(user["password"])
    u.save()
    profile = UserProfile(user=u)
    profile.currency = user["currency"]
    profile.save()


def add_prize(prize):
    p = Prize.objects.get_or_create(prizeName=prize["name"])[0]
    p.prizeValue = prize["value"]
    p.prizeRarity = prize["rarity"]
    p.save()
    return p


def add_achievement(achieve):
    a = Achievement.objects.get_or_create(achievementName=achieve["name"])[0]
    a.achievementDescription = achieve["description"]
    a.save()
    return a


populate()
