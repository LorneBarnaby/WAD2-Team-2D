from django.test import TestCase
from CR8.models import UserProfile, User, Prize
from CR8.rarity import RARITY


class UserProfileTest(TestCase):
    def setUp(self):
        self.prize = Prize(prizeRarity=RARITY.RARE, prizeName="Test Case Prize")
        self.prize.save()

    def test_create_prize(self):
        self.assertEqual(1, Prize.objects.count())

    def test_prize_name(self):
        self.assertEqual("Test Case Prize", Prize.objects.get(id=self.prize.id).prizeName)

    def test_set_prize_name(self):
        self.prize.prizeName = "Changed"
        self.prize.save()
        self.assertEqual("Changed", Prize.objects.get(id=self.prize.id).prizeName)

    def test_set_prize_rarity(self):
        self.prize.prizeRarity = str(RARITY.COMMON)
        self.prize.save()
        self.assertEqual(str(RARITY.COMMON), Prize.objects.get(id=self.prize.id).prizeRarity)

