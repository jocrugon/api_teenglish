from rest_framework import generics
from rest_framework.response import Response

from apiBackend.api.serializers.exercise_serializers import ExerciseSerializer, ExerciseByCategorySerializer, OptionsByExerciseSerializer
from apiBackend.models import List_exercises_category, List_options_exercise
from users.authentication_mixins import Authentication

"""Exercise details"""
class ExerciseRetrieveAPIView(Authentication, generics.RetrieveAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)


"""Exercises by category"""
class ExerciseByCategoryAPIView(Authentication,generics.RetrieveAPIView):
    serializer_class = ExerciseByCategorySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get(self, request, pk=None):
        exerciseByCategory = List_exercises_category.objects.filter(category = pk).all()
        exercise_serializer = ExerciseByCategorySerializer(exerciseByCategory, many=True)
        return Response(exercise_serializer.data)


"""Options by Exercise"""
class OptionsByExerciseAPIView(Authentication,generics.RetrieveAPIView):
    serializer_class = OptionsByExerciseSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request, pk=None):
        optionByExercise = List_options_exercise.objects.filter(exercise = pk).all()
        option_serializer = OptionsByExerciseSerializer(optionByExercise, many = True)
        return Response(option_serializer.data)
    
