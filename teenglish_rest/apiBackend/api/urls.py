from sqlite3 import paramstyle
from django.urls import path
from apiBackend.api.views.general_views import *

urlpatterns = [
    #get list
    path('category/', CategoryAPIView.as_view(), name = 'category'),
    path('exercise/', list_exercises, name = 'lista de exercicios'),
    #get details 
    path('exercise/category/<int:categoryID>/', exercise_by_category, name = 'lista de exercicios por categoria'), 
    path('exercise/<int:pk>', exercise_by_id, name = 'detalle de ejercicio por id'),
    #get list and post
    path('student/', student_view, name = 'student create and view all'),
    #get student  and update por ID
    path('student/<int:pk>/',student_detail_and_update, name ='obtener id con un solo id y actualizar'),
    #get options by idExercise
    path('options/<int:exerciseID>', options_by_exerciseId, name='obtener lista de optiones por id de ejercicio')
    
]