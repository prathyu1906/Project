from django.contrib import admin

from .models import Cricketteam
# Register your models here.

class CricketteamAdmin(admin.ModelAdmin):
    list_display = ['id','name','player_no','age','total_runs']

admin.site.register(Cricketteam,CricketteamAdmin)