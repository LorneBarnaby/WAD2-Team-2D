from population_data_and_methods import generate_user_lists, generate_prize_lists
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cr8_project.settings")
import django

django.setup()
from CR8.models import UserProfile
from django.contrib.auth.models import User


def populate():
    prize_list = generate_prize_lists()
    user_list = generate_user_lists()
    for user in user_list:
        add_user(user)


def add_user(user):
    u = User(username=user["username"])
    u.set_password(user["password"])
    u.save()
    profile = UserProfile(user=u)
    profile.currency = user["currency"]
    profile.save()
    print(profile)


populate()
