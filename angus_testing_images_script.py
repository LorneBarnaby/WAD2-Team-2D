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


prize_list = generate_prize_lists()
user_list = generate_user_lists()
achievement_list = generate_achievement_lists()


def user(user_list):
    for i in range(1, (len(user_list) + 1)):
        profile = UserProfile.objects.get(id=i)
        filename = user_list[i - 1]["username"] + ".jpg"
        try:
            dir = os.path.join(os.getcwd(), "tmp/prof/" + filename)
            profile.profileImage.save(f"{filename}", File(open(dir, "rb")))
        except:
            noProfFilename = "none.jpg"
            dir = os.path.join(os.getcwd(), "tmp/prof/" + noProfFilename)
            profile.profileImage.save(f"{filename}", File(open(dir, "rb")))


def prize(prize_list):
    for i in range(1, len(prize_list)):
        prize = Prize.objects.get(id=i)
        filename_in = str(i) + ".jpg"
        filename_out = prize_list[i - 1]["name"] + ".jpg"
        dir = os.path.join(os.getcwd(), "tmp/prize/" + filename_in)
        prize.prizeImage.save(f"{filename_out}", File(open(dir, "rb")))


user(user_list)
prize(prize_list)
