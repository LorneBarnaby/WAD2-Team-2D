from django.contrib.auth import authenticate
from django.test import TestCase
from django.urls import reverse

from CR8.models import UserProfile, User, Prize
from CR8.rarity import RARITY
from django.test import Client

class ProfileTest(TestCase):


    def setUp(self):
        self.testCasePass = "ExamplePassword1!"
        self.testCaseUserName = "testCaseUser"
        self.testCaseUser = User.objects.create_user(username=self.testCaseUserName, password=self.testCasePass)
        self.testCaseUser.save()
        self.profile = UserProfile(user=self.testCaseUser, currency=100)
        self.profile.save()
        self.client = Client()

    def test_status_is_200(self):
        response = self.client.get(reverse('cr8:index'))
        self.assertEqual(200, response.status_code)

    def test_context_no_login(self):
        response = self.client.get(reverse('cr8:index'))
        context = response.context
        print(context)

    def test_context_login(self):
        self.client.post(reverse('cr8:login'), {'username': self.testCaseUserName, 'password': self.testCasePass},
                         follow=True)
        response = self.client.get(reverse('cr8:index'))
        context = response.context
        self.assertIs(100, response.context['user_currency'])
        self.assertEqual(self.profile, context['user_profile'])
        self.assertQuerysetEqual([], response.context['user_prize_list'])



