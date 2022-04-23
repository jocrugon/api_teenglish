from os import stat
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from apiBackend.models import *
from apiBackend.api.serializers.general_serializers import *
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

class StudentByIdAccount(Authentication, generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id =pk, state = True).first()


    
    def patch(self, request,pk= None):
        if self.get_queryset(pk):
            student_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existre un estudiante con esos datos!'},status=status.HTTP_400_BAD_REQUEST) 
        
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            student_serializer = self.serializer_class(self.get_queryset(pk),data=request.data)

            if student_serializer.is_valid():
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_200_OK)
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



