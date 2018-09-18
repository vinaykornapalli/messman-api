from django.db import models
from django.contrib.auth.models import User






# Create your models here.
class WeekSchedule(models.Model):
     user = models.OneToOneField(User , on_delete=models.CASCADE)
     def __str__(self):
        return "{}'s Schedule".format(self.user.username)

class Day(models.Model):
     mess_day = models.CharField(max_length = 3 , unique = True)
     breakfast = models.CharField(max_length = 50 ,blank = True)
     lunch = models.CharField(max_length = 50 , blank=True)
     snacks = models.CharField(max_length = 50 , blank=True)
     dinner = models.CharField(max_length = 50 ,blank=True) 
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     week = models.ForeignKey(WeekSchedule,on_delete=models.CASCADE)