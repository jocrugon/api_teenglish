from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apiBackend.models import *
from apiBackend.api.serializers.general_serializers import *

from base.api import GeneralListApiView



"""GETS"""
#list de categorias
class CategoryAPIView(GeneralListApiView):
    serializer_class = CategorySerializer

#list de themes in Learning
class LearningAPIView(GeneralListApiView):
    serializer_class = LearningSerializer

class OptionsByThemeAPIView(generics.RetrieveAPIView):
    serializer_class = OptionsByThemeSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get(self, request, pk=None):
        optionByTheme = List_options_learning.objects.filter(learning = pk).all()
        option_serializer = OptionsByThemeSerializer(optionByTheme, many = True)
        return Response(option_serializer.data)





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


"""   """
