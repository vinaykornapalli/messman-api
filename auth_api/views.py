from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import LoginSerializer
from django.contrib.auth import login as django_login , logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        django_login(user, request)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key}, status= 200)


class Logout(APIView):
    authentication_classes = (TokenAuthentication)

    def post(self, request):
        django_logout(request)
        return Response(status=204)

