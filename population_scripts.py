from setup.scripts.population_data_and_methods import (
    generate_user_lists,
    generate_prize_lists,
    generate_achievement_lists,
)
import os
from shutil import copyfile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cr8_project.settings")
import django

django.setup()
from CR8.models import UserProfile, Prize, Achievement
from django.contrib.auth.models import User
from django.core.files import File


def populate():
    # this is the main backbone of the population script, mostly it just calls
    # other functions with the generated dicts with the field as a key and the data as a value
    prize_list = generate_prize_lists()
    user_list = generate_user_lists()
    achievement_list = generate_achievement_lists()
    # we need to copy the no profile image
    copy_no_profile_image()

    profile_check = input("""
Enter yes or y to add dummy user data for testing, otherwise enter
n or no to skip this and just add achievements, prizes and a default profile picture
> """).casefold()

    acceptable_responses = {"y", "yes", "n", "no"}

    while profile_check not in acceptable_responses:
        profile_check = input("""
Error I don't recognise that response
Enter yes or y to add dummy user data for testing, otherwise enter
n or no to skip this and just add achievements, prizes and a default profile picture
> """).casefold()

    if profile_check in {"y", "yes"}:
        print("true")
        add_profiles = True
    else:
        print("false")
        add_profiles = False

    for prize in prize_list:
        prize_django_object = add_prize(prize)
        # passing the prize django object to the add image function
        add_image_prize(prize_django_object, prize)

    for achieve in achievement_list:
        achieve_django_object = add_achievement(achieve)
        add_image_achievement(achieve_django_object, achieve)

    # adds profiles in a simlar way to the other functions if the user has declared
    # that they want to
    if add_profiles:
        for user in user_list:
            profile_django_object = add_user(user)
            add_prizes_to_user(profile_django_object, user)
            add_achievements_to_user(profile_django_object, user)
            add_image_user(profile_django_object, user)


def copy_no_profile_image():
    # copying no profile image, if the file or folder already exists
    # python gets arsey, so we just encase these in a try except as
    # if the file/folder exists there's no need to make/copy it
    folder = "media/profile_images"
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    source = os.path.join(os.getcwd(), "setup/prof/none.jpg")
    dest = os.path.join(os.getcwd(), folder + "/none.jpg")
    try:
        copyfile(source, dest)
    except:
        pass


def add_user(user):
    #using the builtin django functionality to create a user with
    # the username given by the dict
    username = user["username"]
    u = User.objects.get_or_create(username=username)[0]
    u.set_password(user["password"])
    u.save()
    # we now pass that user to userProfile set currency and save it
    profile = UserProfile.objects.get_or_create(user=u)[0]
    profile.currency = user["currency"]
    profile.save()
    return profile


def add_prize(prize):
    # similar to above but with prizes
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
    a.achievementType = achieve["type"]
    a.achievementCriteriaExpectedVal = achieve["requirements"]
    a.save()
    return a


def add_image_user(profile, user_data):
    # adds profile image to the dummy user data - if they have one - if not
    # we just skip
    filename = user_data["username"] + ".jpg"

    try:
        dir = os.path.join(os.getcwd(), "setup/prof/" + filename)
        profile.profileImage.save(f"{filename}", File(open(dir, "rb")))
    except:
        pass


def add_image_prize(prize, prize_data):
    # fairly simple just assosciates an image with a prize in the db
    filename = prize_data["imagename"]
    dir = os.path.join(os.getcwd(), "setup/prize/" + filename)
    prize.prizeImage.save(filename, File(open(dir, "rb")))


def add_image_achievement(achieve, achieve_data):
    # as above
    filename = achieve_data["imagename"]
    dir = os.path.join(os.getcwd(), "setup/achieve/" + filename)
    achieve.achievementImage.save(filename, File(open(dir, "rb")))


def add_prizes_to_user(user, user_dict):
    # assosciates prizes with user for the dummy data
    prizeList = user_dict["prizeList"]

    for prize in prizeList:
        prize_django_object = Prize.objects.get(prizeName=prize)
        user.prizes.add(prize_django_object)

    user.save()


def add_achievements_to_user(user, user_dict):
    # adds achievements to user
    achieve_list = user_dict["achieveList"]

    for achieve in achieve_list:
        achieve_django_object = Achievement.objects.get(achievementName=achieve)
        user.achievements.add(achieve_django_object)

    user.save()


populate()
