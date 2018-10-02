
# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Day ,WeekSchedule
from .serializers import (DayListSerializer ,
 WeekScheduleSerializer ,
 WeekScheduleResponseSerializer
)
# Create your views here.




class CreateDay(generics.CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DayListSerializer

class UpdateDay(generics.UpdateAPIView):
    queryset = Day.objects.all()
    serializer_class = DayListSerializer




#getting list of days from frontend and storing them in days

class CreateWeekSchedule(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self , request):
        serializer = WeekScheduleSerializer(data=request.data , many =True)
        if serializer.is_valid(raise_exception=True):
            print(request.user.id)
            p = WeekSchedule.objects.create(user=request.user)
            p.save()
            serializer.save(week=p)
            days = Day.objects.filter(week = p).values()
            table = []
            for day in days:
                tmp =  WeekScheduleSerializer(data=day)
                if tmp.is_valid(raise_exception=True):
                    table.append(tmp.validated_data)
            data = {'table' : table , "week_id" : p.id}
        return Response(data=data)

            

    