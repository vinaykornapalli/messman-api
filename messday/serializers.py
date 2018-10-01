from . import models
from rest_framework import serializers




class DaySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Day
    fields = ['id' , 'mess_day' , 'breakfast' , 'lunch' ,'snacks', 'dinner']

class WeekScheduleSerializer(serializers.Serializer):
  day = serializers.CharField(max_length=3)
  breakfast = serializers.CharField(max_length=100)
  lunch =  serializers.CharField(max_length=100)
  snacks = serializers.CharField(max_length=100)
  dinner = serializers.CharField(max_length=100)
  
  def validate(self ,data):
    day = data.get("day", "")
    breakfast = data.get("breakfast" ,"")
    lunch = data.get("lunch" ,"")
    snacks = data.get("snacks" ,"")
    dinner = data.get("dinner" ,"")
    #user validation to be done
    return data
