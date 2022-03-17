from django.contrib.auth import authenticate
from django.test import TestCase
from django.urls import reverse

from CR8.models import UserProfile, User, Prize
from CR8.rarity import RARITY
from django.test import Client


class IndexPageTest(TestCase):

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
        self.assertIs(None, response.context['user_profile'])
        self.assertIs(None, response.context['user_prize_list'])
        self.assertIs(None, response.context['user_currency'])

    def test_context_login(self):
        self.client.post(reverse('cr8:login'), {'username': self.testCaseUserName, 'password': self.testCasePass},
                         follow=True)
        response = self.client.get(reverse('cr8:index'))
        context = response.context
        self.assertIs(100, response.context['user_currency'])
        self.assertEqual(self.profile, context['user_profile'])
        self.assertQuerysetEqual([], response.context['user_prize_list'])


    def test_context_login_has_prizes(self):
        self.client.post(reverse('cr8:login'), {'username': self.testCaseUserName, 'password': self.testCasePass},
                         follow=True)
        # prize = Prize(prizeRarity=RARITY.RARE, prizeName="Test Case Prize")
        # prize.save()
        # self.profile.prizes.add(prize)
        # self.profile.save()
        response = self.client.get(reverse('cr8:index'))
        context = response.context
        self.assertIs(100, response.context['user_currency'])
        self.assertEquals(self.profile, context['user_profile'])
        # self.assertEquals(1, len(response.context['user_prize_list']))

    def test_html_no_login(self):
        response = self.client.get(reverse('cr8:index'))
        self.assertContains(response, 'Login to see your currency')
        self.assertContains(response, 'Login to earn and see your prizes!')

    def test_html_login(self):
        self.client.post(reverse('cr8:login'), {'username': self.testCaseUserName, 'password': self.testCasePass},
                         follow=True)
        response = self.client.get(reverse('cr8:index'))
        self.assertNotContains(response, 'Login to see your currency')
        self.assertNotContains(response, 'Login to earn and see your prizes!')


