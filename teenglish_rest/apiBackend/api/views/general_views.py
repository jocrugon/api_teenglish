import re
from unicodedata import category
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apiBackend.models import *
from apiBackend.api.serializers.general_serializers import *



"""GETS"""
#list de categorias
class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(state=True)

#list de todos los ejercicios
@api_view(['GET'])
def list_exercises(request):
    list_exercises = Exercise.objects.all()
    list_exercises_serializer = ExerciseSerializer(list_exercises, many = True)
    return Response(list_exercises_serializer.data)
    """ exercises = ExerciseSerializer(list_exercises, many = True).data
    return JsonResponse({'status':'ok','exercises':exercises}, safe=False) """


#list de ejercicio por categoría
@api_view(['GET'])
def exercise_by_category(request, categoryID = None):
    
    if request.method == 'GET':
        exercise = List_exercises_category.objects.filter(category = categoryID).all()
        exercise_serializer = ListExercise_by_category(exercise, many=True)
        return Response(exercise_serializer.data)


#list de ejercicio por id
@api_view(['GET'])
def exercise_by_id(request, pk = None):
    
    if request.method == 'GET':
        exercise = Exercise.objects.filter(id = pk).all()
        exercise_serializer = ExerciseSerializer(exercise, many=True)
        return Response(exercise_serializer.data)


"""get options by ExerciseId"""
@api_view(['GET'])
def options_by_exerciseId(request, exerciseID = None):
    
    if request.method == 'GET':
        options = List_options_exercise.objects.filter(exercise = exerciseID).all()
        options_serializer = ListOptions_by_exerciseId(options, many=True)
        return Response(options_serializer.data)


"""list de estudiantes y post"""

@api_view(['GET','POST'])
def student_view(request):
    if request.method == 'GET':
        student = Student.objects.all()
        student_serializer = StudentSerializer(student, many=True)
        return Response(student_serializer.data)

    elif request.method == 'POST':
        student_serializer = StudentSerializer(data = request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        return Response(student_serializer.errors)



"""get student por id y update"""
@api_view(['GET','PUT'])
def student_detail_and_update(request, pk = None):

    if request.method == 'GET':
        student = Student.objects.filter(id = pk).first()
        student_serializer = StudentSerializer(student)
        return Response(student_serializer.data)
    elif request.method == 'PUT':
        student = Student.objects.filter(id = pk).first()
        student_serializer = StudentSerializer(student, data = request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        return Response(student_serializer.errors)
