from os import stat
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from teenglish.models import *
from teenglish.api.serializers.general_serializers import *
from users.authentication_mixins import Authentication


from base.api import GeneralListApiView


"""GETS"""
#list de categorias
class CategoryAPIView(Authentication,GeneralListApiView):
    serializer_class = CategorySerializer

#list de themes in Learning
class LearningAPIView(Authentication,GeneralListApiView):
    serializer_class = LearningSerializer


class OptionsByThemeAPIView(Authentication,generics.RetrieveAPIView):
    serializer_class = OptionsByThemeSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get(self, request, pk=None):
        optionByTheme = List_options_learning.objects.filter(learning = pk).all()
        option_serializer = OptionsByThemeSerializer(optionByTheme, many = True)
        return Response(option_serializer.data)

class StudentByIdAccount(Authentication, generics.RetrieveAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request, idAccount = None):
        studentByIdAccount = Student.objects.filter(user=idAccount).first()
        student_serializer = StudentSerializer(studentByIdAccount)
        return Response(student_serializer.data);

class UpdateScoreInStudent(Authentication, generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id =pk, state = True).first()

    
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            scoreStudent_serializer = self.serializer_class(self.get_queryset(pk),data=request.data)

            if scoreStudent_serializer.is_valid():
                scoreStudent_serializer.save()
                return Response(scoreStudent_serializer.data, status=status.HTTP_200_OK)
            return Response(scoreStudent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)