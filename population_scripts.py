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

    image_check = input(
        """
Enter s to skip adding of images, enter anything else to not skip
might be wise to skip if you've done it before
as it'll just duplicate lots of images
> """
    )

    add_images = True
    if image_check == "s" or image_check == "S":
        add_images = False

    for user in user_list:
        profile_django_object = add_user(user)
        if add_images:
            add_image_user(profile_django_object, user)

    for prize in prize_list:
        prize_django_object = add_prize(prize)
        if add_images:
            add_image_prize(prize_django_object, prize)

    for achieve in achievement_list:
        achieve_django_object = add_achievement(achieve)
        if add_images:
            add_image_achievement(achieve_django_object, achieve)


def add_user(user):
    username = user["username"]
    u = User.objects.get_or_create(username=username)[0]
    u.set_password(user["password"])
    u.save()
    profile = UserProfile.objects.get_or_create(user=u)[0]
    profile.currency = user["currency"]
    profile.save()
    return profile


def add_prize(prize):
    prize_name = prize["name"]
    p = Prize.objects.get_or_create(prizeName=prize_name)[0]
    p.prizeValue = prize["value"]
    p.prizeRarity = prize["rarity"]
    p.save()
    return p


def add_achievement(achieve):
    achievement_name = achieve["name"]
    a = Achievement.objects.get_or_create(achievementName=achievement_name)[0]
    a.achievementDescription = achieve["description"]
    a.save()
    return a


def add_image_user(profile, user_data):
    filename = user_data["username"] + ".jpg"

    try:
        dir = os.path.join(os.getcwd(), "tmp/prof/" + filename)
        profile.profileImage.save(f"{filename}", File(open(dir, "rb")))
    except:
        pass


def add_image_prize(prize, prize_data):
    filename = prize_data["imagename"]
    dir = os.path.join(os.getcwd(), "tmp/prize/" + filename)
    prize.prizeImage.save(filename, File(open(dir, "rb")))


def add_image_achievement(achieve, achieve_data):
    filename_in = str(achieve.id) + ".jpg"
    filename_out = achieve_data["name"] + ".jpg"
    dir = os.path.join(os.getcwd(), "tmp/achieve/" + filename_in)
    achieve.achievementImage.save(f"{filename_out}", File(open(dir, "rb")))


populate()
