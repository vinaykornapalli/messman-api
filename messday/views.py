
# Create your views here.

from django.shortcuts import render
from rest_framework import generics


from .models import Day ,WeekSchedule
from .serializers import DaySerializer , WeekScheduleSerializer
# Create your views here.




class CreateDay(generics.CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class UpdateDay(generics.UpdateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class CreateWeekSchedule(generics.CreateAPIView):
    queryset = WeekSchedule.objects.all()
    serializer_class  = WeekScheduleSerializer

