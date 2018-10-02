from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import LoginSerializer
from django.contrib.auth import login as django_login , logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist
class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True) 
        user = serializer.validated_data["user"]
        django_login(request ,user)
        print(user.__dict__)
        token, created = Token.objects.get_or_create(user=user)
        has_weekschedule = True
        try:
            user.weekschedule
        except ObjectDoesNotExist:
            has_weekschedule = False

        return Response({"token":token.key ,
        "user_id" :user.pk ,
         "email" : user.email , 
         "is_active" : user.is_active ,
          "is_staff" : user.is_staff,
          "username" : user.username,
          "has_schedule" : has_weekschedule
          }, status= 200)


class Logout(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        django_logout(request)
        return Response(status=204)

