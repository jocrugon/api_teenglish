from dataclasses import field
from apiBackend.models import *

from rest_framework import serializers


""" list category """
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        exclude = ('state',)


"""list exercise"""
class Type_exerciseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Type_exercise
        exclude = ('state',)


class Message_motivationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message_motivation
        exclude = ('state',)
            

class ExerciseSerializer(serializers.ModelSerializer):
    message_motivation = Message_motivationSerializer()
    type_exercise = Type_exerciseSerializer()
    
    class Meta:
        model = Exercise
        exclude = ('state',)


"""list options by ExerciseId"""
class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = '__all__'


class ListOptions_by_exerciseId(serializers.ModelSerializer):

    option = OptionSerializer()
    
    class Meta:
        model = List_options_exercise
        fields = ['option']


""" list exercise by category """
class ListExercise_by_category(serializers.ModelSerializer):
   
    exercise = ExerciseSerializer()
    class Meta:
        model = List_exercises_category
        fields = ['exercise']


"""Sign up"""
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

