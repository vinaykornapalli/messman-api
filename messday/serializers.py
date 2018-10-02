from .models import Day , WeekSchedule
from rest_framework import serializers



class DayListSerializer(serializers.ListSerializer):
  def create(self ,validated_data):
    days = [Day(**item) for item in validated_data]
    return Day.objects.bulk_create(days)


class WeekScheduleSerializer(serializers.Serializer):
  mess_day = serializers.CharField(max_length=3)
  breakfast = serializers.CharField(max_length=100)
  lunch =  serializers.CharField(max_length=100)
  snacks = serializers.CharField(max_length=100)
  dinner = serializers.CharField(max_length=100)
  
  def validate(self ,data):
    mess_day = data.get("mess_day", "")
    breakfast = data.get("breakfast" ,"")
    lunch = data.get("lunch" ,"")
    snacks = data.get("snacks" ,"")
    dinner = data.get("dinner" ,"")
    #user validation to be done
    return data

  class Meta:
    list_serializer_class = DayListSerializer
  
class WeekScheduleResponseSerializer(serializers.ModelSerializer):

  class Meta:
    model = Day
    fields = ('mess_day' , 'breakfast' , 'lunch' , 'dinner')