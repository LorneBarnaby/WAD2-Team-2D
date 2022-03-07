from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from CR8.models import UserProfile, Prize, Achievement
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.urls import reverse


# Create your views here.
def index(request):
    # TEST VIEW - to check we can display user profile images in templates

    userProfile = UserProfile.objects.get(user__username="JackKilpack")

    context_dict = {}
    context_dict['UserProfile'] = userProfile

    print(userProfile.profileImage.url)
    return render(request, 'cr8/index.html', context=context_dict)


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

    return render(request, 'cr8/leaderboard.html', context=context_dict)


def contact_us(request):
    return render(request, 'cr8/contact-us.html')

def faqs(request):
    return render(request, 'cr8/faqs.html')

def profile(request,username):

    context_dict = {}

    if request.user.is_authenticated and request.user.username == username:
        context_dict['is_current_user'] = True
    else:
        context_dict['is_current_user'] = False

    try:
        user_profile = UserProfile.objects.get(user__username=username)
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