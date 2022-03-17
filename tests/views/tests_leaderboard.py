from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from CR8.models import UserProfile


class LeaderboardTests(TestCase):
    lorne = ""

    def setUp(self):
        u1 = User(username="LorneBarnaby")
        u1.save()
        u1.set_password("Fake Password 19.8")
        lorne = UserProfile(user=u1)
        lorne.currency = 4000
        lorne.save()

    def test_response(self):
        response = self.client.get(reverse("cr8:leaderboard"))
        context = response.context
        print(context)
        self.assertEqual(response.status_code, 200)

    def test_2(self):
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertContains(response,)
