from django import template
from CR8.models import UserProfile
from CR8.rarity import RARITY

register = template.Library()


@register.filter
def get_slug(user):
    profile = UserProfile.objects.get(user__username=user.username)
    return profile.username_slug


@register.filter
def get_rarity(prize):
    return RARITY.get_int_value(prize.prizeRarity)