from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from CR8.models import UserProfile


class LeaderboardTests(TestCase):
    def setUp(self):
        self.userList = [
            "Harry",
            "Barry",
            "Carry",
            "kkk",
            "charlie",
            "steve",
            "iii",
            "jjj",
            "ppp",
            "Sharon",
            "ttt",
            "ooo",
            "cat",
        ]

    def test_response(self):
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertEqual(response.status_code, 200)

    def test_no_users(self):
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertContains(response, "Try making some friends")

    def add_users(self, iterations):
        sharon = ""
        for i in range(iterations):
            user = User(username=self.userList[i])
            user.set_password("Fake Password 19.8")
            user.save()
            profile = UserProfile(user=user)
            profile.save()
            if self.userList[i] == "Sharon":
                sharon = profile

        return sharon

    def test_10_users(self):
        testProfile = self.add_users(10)
        testProfile.currency = 12
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertContains(response, "Sharon")

    def test_users_cutoff(self):
        testProfile = self.add_users(13)
        testProfile.currency = 0
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertNotContains(response, "<h5>11</h5>")

    def test_one_user_no_text(self):
        self.add_users(1)
        response = self.client.get(reverse("cr8:leaderboard"))
        self.assertNotContains(response, "Try making some friends")
