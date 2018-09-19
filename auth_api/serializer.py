from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import exceptions

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length= 25)
    password = serializers.CharField(max_length= 25)

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        if username and password :
            user = authenticate(username="username", password="password")
            if user:
                if user.is_active():
                    data['user'] = user
                else:
                    msg = "This user is not active"
                    exceptions.ValidationError(msg)
            else:
                msg = "The given credentials are invalid"
                exceptions.ValidationError(msg)
        else:
            msg = "Please fillout the username and password feilds"
            exceptions.ValidationError(msg)

        return data
