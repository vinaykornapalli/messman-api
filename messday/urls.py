from django.conf.urls import url , include 
from . import views

urlpatterns =[
   
    url('^menu/$' , views.CreateDay.as_view()),
    url('^schedule/$' , views.CreateWeekSchedule.as_view())
  
]