from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','last_name_p','last_name_m')
