from django.contrib import admin
from .models import UserProfile,Achievement,Prize


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Achievement)
admin.site.register(Prize)