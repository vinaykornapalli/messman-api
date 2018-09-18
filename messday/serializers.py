from . import models
from rest_framework import serializers




class DaySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Day
    fields = ['id' , 'mess_day' , 'breakfast' , 'lunch' ,'snacks', 'dinner']

class WeekScheduleSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.WeekSchedule
    fields = [ 'user']