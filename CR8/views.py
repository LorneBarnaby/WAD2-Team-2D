from django.shortcuts import render
from django.http import HttpResponse
from CR8.models import UserProfile

# Create your views here.
def index(request):

    userProfile = UserProfile.Objects.get(username='JackKilpack')

    context_dict = {}
    context_dict['UserProfile'] = userProfile



    return render(request, 'cr8/index.html', context=context_dict)
