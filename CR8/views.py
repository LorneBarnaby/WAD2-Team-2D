from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import json

from CR8.models import UserProfile, Prize, Achievement
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

from CR8.rarity import RARITY
from random import randint, choices


# Create your views here.
def index(request):

    context_dict = {}

    # Get the user profile instance associated with the current request, if it exists
    # Store it in the context dictionary if so
    try:
        user_profile = UserProfile.objects.get(user__username=request.user)
        user_prize_list = Prize.objects.filter(userprofile=user_profile).order_by('-prizeValue')[:6]
        user_currency = user_profile.currency
        context_dict['user_profile'] = user_profile
        context_dict['user_prize_list'] = user_prize_list
        context_dict['user_currency'] = user_currency

    except UserProfile.DoesNotExist:
        context_dict['user_profile'] = None
        context_dict['user_prize_list'] = None
        context_dict['user_currency'] = None

    return render(request, 'cr8/index.html', context=context_dict)


@login_required
def generate_prizes(request):
    # Choose a rarity based on thier weights as defined in the rarity enum
    chosen_rarity = choices([str(r) for r in RARITY], [r.rarity for r in RARITY])

    # find all prizes with that given rarity
    items = Prize.objects.filter(prizeRarity=chosen_rarity[0]).all()

    # choose randomly from that list of items
    chosen = items[randint(0, items.count() - 1)]

    user_profile = UserProfile.objects.get(user__username=request.user)

    # check that the user has enough currency to buy a CR8
    if user_profile.currency >= 20:

        user_profile.currency -= 20
        user_profile.prizes.add(chosen)
        user_profile.save()

        # load the values into a dictionary
        values = {"prizeName": chosen.prizeName, "prizeRarity": chosen.prizeRarity,
                  "prizeValue": chosen.prizeValue, "prizeImg": chosen.prizeImage.url,
                  "updated_currency": user_profile.currency}

    else:

        values = {"prizeName": "Not enough currency!", "prizeImg": "",
                  "updated_currency": user_profile.currency}

    # return the new JSON object created from the dictionary to the browser
    return HttpResponse(json.dumps(values))




def sign_up(request):
    # If the request method is POST, process form data
    # Otherwise show the registration form if a GET request was made by a new user
    # or the edit profile form if a GET request was made by an existing user
    registered = False
    if request.method == 'POST':

        # If the user is authenticated, they are editing their profile so store the edit profile form
        if request.user.is_authenticated:
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = UserProfileForm(request.POST, instance=UserProfile.objects.get(user=request.user))
        # Otherwise this is a new user signing up so store the regular form
        else:
            user_form = UserForm(request.POST)
            profile_form = UserProfileForm(request.POST)

        # If the form submitted is valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save the submitted user data to a user instance
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Save the submitted profile data to a user profile instance
            # This includes any submitted profile image or the default profile image otherwise
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profileImage' in request.FILES:
                profile.profileImage = request.FILES['profileImage']
            else:
                profile.profileImage = "profile_images/none.jpg"

            profile.save()

            # Once the user's data has been saved to the database, log them in
            registered = True
            login(request, user)

            # If the user who made the request was already registered, this means they were editing their profile
            # so just return them to their profile page
            if request.user.is_authenticated:
                return redirect(reverse('cr8:profile',kwargs={'username_slug':UserProfile.objects.get(user=request.user).username_slug}))
            # Otherwise this was an entirely new user so redirect them to the index page
            else:
                return redirect(reverse('cr8:index'))

        # If any form validation errors were encountered, print them
        else:
            print(user_form.errors, profile_form.errors)

    # In this case a GET request was made
    else:
        # If the user who made the request is already logged in, return an edit profile form
        if request.user.is_authenticated:
            user_form = UserForm(instance=request.user)
            profile_form = UserProfileForm(instance=UserProfile.objects.get(user=request.user))
        # Otherwise the user is trying to sign up so return the sign up form
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()


    return render(request, 'cr8/sign_up.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'edit_mode':request.user.is_authenticated})


def about_us(request):
    return render(request, 'cr8/about-us.html')

def leaderboard(request):

    user_profile_list = UserProfile.objects.order_by('-currency')

    context_dict = {}

    context_dict["user_profile_list"] = user_profile_list

    curr_position_in_leaderboard = None
    if request.user.is_authenticated:
        for leaderboard_index, user_profile in enumerate(user_profile_list):
            if user_profile.user.username == request.user.username:
                curr_position_in_leaderboard = (leaderboard_index + 1)
        context_dict['curr_position_in_leaderboard'] = curr_position_in_leaderboard

    return render(request, 'cr8/leaderboard.html', context=context_dict)


def contact_us(request):
    return render(request, 'cr8/contact-us.html')

def faqs(request):
    return render(request, 'cr8/faqs.html')

def profile(request,username_slug):

    context_dict = {}

    if request.user.is_authenticated and request.user.username == UserProfile.objects.get(username_slug=username_slug).user.username:
        context_dict['is_current_user'] = True
    else:
        context_dict['is_current_user'] = False

    try:
        user_profile = UserProfile.objects.get(username_slug=username_slug)
        user_prize_list = Prize.objects.filter(userprofile=user_profile)
        user_prize_list = user_prize_list.order_by('-prizeValue')
        user_achievement_list = Achievement.objects.filter(userprofile=user_profile)
        unclaimed_achievement_list = Achievement.objects.exclude(userprofile=user_profile)
        user_currency = user_profile.currency

        context_dict['user_profile'] = user_profile
        context_dict['user_prize_list'] = user_prize_list
        context_dict['user_achievement_list'] = user_achievement_list
        context_dict['user_currency'] = user_currency
        context_dict['unclaimed_achievement_list'] = unclaimed_achievement_list

    except UserProfile.DoesNotExist:
        context_dict['user_profile'] = None
        context_dict['user_prize_list'] = None
        context_dict['user_achievement_list'] = None
        context_dict['user_currency'] = None
        context_dict['unclaimed_achievement_list'] = None

    return render(request, 'cr8/profile.html', context=context_dict)

@login_required
def claim_achievement(request):

    achievement_id = request.GET['achievement_id']
    json_dict = {}

    try:
        user_profile = UserProfile.objects.get(user__username=request.user)
        achievement = Achievement.objects.get(id=achievement_id)
        json_dict['achievementName'] = achievement.achievementName
        json_dict['achievementDescription'] = achievement.achievementDescription
        json_dict['achievementImage'] = achievement.achievementImage.url

    except UserProfile.DoesNotExist:
        user_profile = None

    except Achievement.DoesNotExist:
        achievement = None

    if user_profile and achievement:
        # Calls helper function to check achievement criteria is met by the current user
        achievement_criteria_is_met = check_achievement_criteria(user_profile, achievement.achievementType, achievement.achievementCriteriaExpectedVal)
    else:
        achievement_criteria_is_met = False

    if achievement_criteria_is_met:
        json_dict['criteriaIsMet'] = "True"
        user_profile.achievements.add(achievement)
        return HttpResponse(json.dumps(json_dict))
    else:
        json_dict['criteriaIsMet'] = "False"
        return HttpResponse(json.dumps(json_dict))

@login_required
def sell_prize(request):

    prize_id = request.GET['prize_id']
    json_dict = {}

    try:
        user_profile = UserProfile.objects.get(user__username=request.user)
        prize = Prize.objects.get(id=prize_id)
        json_dict['prizeValue'] = prize.prizeValue

    except UserProfile.DoesNotExist:
        user_profile = None

    except Prize.DoesNotExist:
        prize = None

    if user_profile and prize:
        user_profile.prizes.remove(prize)
        user_profile.currency += prize.prizeValue
        user_profile.save()
        json_dict['updated_currency'] = user_profile.currency

    return HttpResponse(json.dumps(json_dict))

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print('user logged in: ', user)
                return redirect(reverse('cr8:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return render(request, 'cr8/login.html', context={"Error":"Error: Invalid username or password!"})
    else:
        return render(request, 'cr8/login.html', context={"Error":None})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('cr8:index'))




# HELPER FUNCTIONS

# Checks if the criteria for the achievement of a given type has been met, if so return true else return false
def check_achievement_criteria(user_profile, type, expected_val):

    if type == "currency" and user_profile.currency >= expected_val:
        return True

    # Other achievement types can be added here in the same way

    return False




