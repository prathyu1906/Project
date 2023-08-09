from django.db import models

# Create your models here.

class Cricketteam(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    player_no = models.IntegerField()
    age = models.IntegerField()
    total_runs = models.IntegerField()
    
    def __str__(self):
        return self.name