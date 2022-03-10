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

    try:
        user_profile = UserProfile.objects.get(user__username=request.user)
        user_prize_list = Prize.objects.filter(userprofile=user_profile).order_by('-prizeValue')[:5]
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
    chosen_rarity = choices([str(r) for r in RARITY], [r.rarity for r in RARITY])
    items = Prize.objects.filter(prizeRarity=chosen_rarity[0]).all()
    chosen = items[randint(0,items.count())]
    values = { "prizeName": chosen.prizeName,"prizeRarity":chosen.prizeRarity, "prizeValue": chosen.prizeValue}
    UserProfile.prizes.add(chosen)
    UserProfile.save()
    return json.dumps(values)




def sign_up(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profileImage' in request.FILES:
                profile.profileImage = request.FILES['profileImage']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'cr8/sign_up.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


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

    if request.user.is_authenticated and request.user.username == username_slug:
        context_dict['is_current_user'] = True
    else:
        context_dict['is_current_user'] = False

    try:
        user_profile = UserProfile.objects.get(username_slug=username_slug)
        user_prize_list = Prize.objects.filter(userprofile=user_profile)
        user_achievement_list = Achievement.objects.filter(userprofile=user_profile)

        context_dict['user_profile'] = user_profile
        context_dict['user_prize_list'] = user_prize_list
        context_dict['user_achievement_list'] = user_achievement_list

    except UserProfile.DoesNotExist:
        context_dict['user_profile'] = None
        context_dict['user_prize_list'] = None
        context_dict['user_achievement_list'] = None

    return render(request, 'cr8/profile.html', context=context_dict)

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
            print(f"Invalid login details: {username}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'cr8/login.html')


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('cr8:index'))