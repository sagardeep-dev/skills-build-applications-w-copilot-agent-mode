from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)

# Optionally, customize User admin if needed
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)