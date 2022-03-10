from django import template
from CR8.models import UserProfile

register = template.Library()


@register.filter
def get_slug(user):
    profile = UserProfile.objects.get(user__username=user.username)
    return profile.username_slug
