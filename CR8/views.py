from django.shortcuts import render
from django.http import HttpResponse
from CR8.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    # TEST VIEW - to check we can display user profile images in templates

    userProfile = UserProfile.objects.get(user__username="JackKilpack")

    context_dict = {}
    context_dict['UserProfile'] = userProfile


    print(userProfile.profileImage.url)
    return render(request, 'cr8/index.html', context=context_dict)
