from django.template.defaultfilters import slugify
from django.test import TestCase
from CR8.models import UserProfile, User, Prize
from CR8.rarity import RARITY


class UserProfileTest(TestCase):
    def setUp(self):
        self.testCaseUser = User(username="testCaseUser")
        self.testCaseUser.save()
        self.profile = UserProfile(user=self.testCaseUser, currency=100)
        self.profile.save()

    def test_create_UserProfile(self):
        self.assertEqual(1, UserProfile.objects.count())

    def test_create_UserProfile_username(self):
        self.assertEqual(self.testCaseUser.username, self.profile.user.username)

    def test_create_UserProfile_slug(self):
        self.assertEqual(slugify(self.testCaseUser.username), self.profile.username_slug)

    def test_add_prizes(self):
        prizes = [
            Prize(prizeName="1", prizeRarity=str(RARITY.COMMON), prizeValue=100),
            Prize(prizeName="2", prizeRarity=str(RARITY.COMMON), prizeValue=101),
        ]
        for p in prizes:
            p.save()
            self.profile.prizes.add(p)
        self.assertEqual(2, self.profile.prizes.count())

    def test_give_currency(self):
        self.profile.currency += 100
        self.profile.save()
        self.assertEqual(200, UserProfile.objects.get(id=self.profile.id).currency)
