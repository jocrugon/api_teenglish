from dataclasses import field
from apiBackend.models import *

from rest_framework import serializers


""" list category """
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        exclude = ('state',)
"""list themes in learning"""
class LearningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Learning
        exclude = ('state',)


class OptionsByThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = List_options_learning
        exclude = ('state',)

    def to_representation(self, instance):
        return {
            'option': instance.option.option,
            
        }



"""Sign up"""
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ('state','created_date','modified_date','deleted_date')

