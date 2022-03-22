from django.test import TestCase
from CR8.models import UserProfile, User, Prize, Achievement
from CR8.rarity import RARITY


class AchievementTest(TestCase):

    def setUp(self) -> None:
        self.achievement = Achievement(
            achievementType="currency",
            achievementName="Test Achievement",
            achievementDescription="A Test Description",
            achievementCriteriaExpectedVal=100
        )
        self.achievement.save()

    def test_create_achievement(self):
        self.assertEqual(1, Achievement.objects.count())

    def test_achievement_name(self):
        self.assertEqual(self.achievement.achievementName, "Test Achievement")

    def test_achievement_expected(self):
        self.assertEqual(self.achievement.achievementCriteriaExpectedVal, 100)

    def test_set_name(self):
        # self.achievement
        self.achievement.achievementName = "Test"
        self.achievement.save()
        self.assertEqual(
            Achievement.objects.get(id=self.achievement.id).achievementName,
            "Test"
        )

    def test_set_description(self):
        self.achievement.achievementDescription = "test"
        self.achievement.save()
        self.assertEqual(
            Achievement.objects.get(id=self.achievement.id).achievementDescription,
            "test"
        )

    def test_set_expected(self):
        self.achievement.achievementCriteriaExpectedVal = 250
        self.achievement.save()
        self.assertEqual(
            Achievement.objects.get(id=self.achievement.id).achievementCriteriaExpectedVal,
            250
        )

    def test_set_type(self):
        self.achievement.achievementType = "test"
        self.achievement.save()
        self.assertEqual(
            Achievement.objects.get(id=self.achievement.id).achievementType,
            "test"
        )
