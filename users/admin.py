from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class AdminViewProfile(admin.ModelAdmin):
    list_display = ['user','date_of_birth']