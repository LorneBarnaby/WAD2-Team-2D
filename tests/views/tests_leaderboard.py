from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from CR8.models import UserProfile


class LeaderboardTests(TestCase):
    def setUp(self):
        pass

    def test_response(self):
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertEqual(response.status_code, 200)

    def test_no_users(self):
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertContains(response, "Try making some friends")

    def test_users_4(self):
        for i in range(8, 14):
            user = User(username=str(i))
            user.set_password("Fake Password 19.8")
            user.save()
            profile = UserProfile(user=user)
            profile.save()
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertContains(response, "<h5>4</h5>")

    def test_users_cutoff(self):
        for i in range(10):
            user = User(username=str(i))
            user.set_password("Fake Password 19.8")
            user.save()
            profile = UserProfile(user=user)
            profile.save()
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertNotContains(response, "<h5>11</h5>")
