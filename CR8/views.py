from django.shortcuts import render
from django.http import HttpResponse
from CR8.models import UserProfile
from .forms import UserForm, UserProfileForm

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


def login(request):
    return render(request, 'cr8/login.html')


def about_us(request):
    return render(request, 'cr8/about-us.html')

def leaderboard(request):
    return render(request, 'cr8/leaderboard.html')


def contact_us(request):
    return render(request, 'cr8/contact-us.html')

def faqs(request):
    return render(request, 'cr8/faqs.html')

def profile(request):
    return render(request, 'cr8/profile.html')
