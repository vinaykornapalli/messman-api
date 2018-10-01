
# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Day ,WeekSchedule
from .serializers import DaySerializer , WeekScheduleSerializer
# Create your views here.




class CreateDay(generics.CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class UpdateDay(generics.UpdateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer




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
            data = {'user' : request.user.id}
        return Response(data=data)

            

