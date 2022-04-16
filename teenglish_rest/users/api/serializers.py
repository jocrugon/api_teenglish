from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        ''' #only with json 
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user'''
        #json and form data
        instance = User()
        instance.name = validated_data.get('name')
        instance.last_name_p = validated_data.get('last_name_p')
        instance.last_name_m = validated_data.get('last_name_m')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance 
    
        
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username':instance['username'],
            'password': instance['password'],
        }


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','last_name_p','last_name_m')
