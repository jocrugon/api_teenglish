from rest_framework import generics
from rest_framework.response import Response

from rest_framework import status

from apiBackend.api.serializers.exercise_serializers import ExerciseSerializer, ExerciseByCategorySerializer, OptionsByExerciseSerializer
from apiBackend.models import List_exercises_category, List_options_exercise, Exercise
from users.authentication_mixins import Authentication

"""Exercise details"""
class ExerciseRetrieveAPIView(Authentication, generics.RetrieveAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get(self, request, pk = None):
        exercise = Exercise.objects.filter(id=pk).first()
        exercise_serilizer = ExerciseSerializer(exercise)

        optionByExercise = List_options_exercise.objects.filter(exercise = pk).all()
        option_serializer = OptionsByExerciseSerializer(optionByExercise, many = True)

        return Response({
            'exercise':exercise_serilizer.data,
            'options': option_serializer.data
            })


"""Exercises by category"""
class ExerciseByCategoryAPIView(Authentication,generics.RetrieveAPIView):
    serializer_class = ExerciseByCategorySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get(self, request, idCategory=None, idStudent = None):
        exerciseByCategory = List_exercises_category.objects.filter( student=idStudent, category = idCategory).all()
        exercise_serializer = ExerciseByCategorySerializer(exerciseByCategory, many=True)
        return Response(exercise_serializer.data)


"""Update List Exercise by categoryid and studentid"""
class UpdateDetailExerciseByStudentAPIView(Authentication, generics.RetrieveUpdateAPIView):
    serializer_class = ExerciseByCategorySerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id =pk, state = True).first()
    
    
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            detailExercise_serializer = self.serializer_class(self.get_queryset(pk),data=request.data)

            if detailExercise_serializer.is_valid():
                detailExercise_serializer.save()
                return Response(detailExercise_serializer.data, status=status.HTTP_200_OK)
            return Response(detailExercise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    
    
