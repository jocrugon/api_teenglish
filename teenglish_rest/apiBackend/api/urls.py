from django.urls import path
from apiBackend.api.views.general_views import *
from apiBackend.api.views.exercise_views import  ExerciseRetrieveAPIView, ExerciseByCategoryAPIView,OptionsByExerciseAPIView

urlpatterns = [
    #get list
    path('category/', CategoryAPIView.as_view(), name = 'category'),
    path('learning/', LearningAPIView.as_view(), name = 'lista de themes in Learning'),
    
    #get details 
    path('exercise/<int:pk>', ExerciseRetrieveAPIView.as_view(), name = 'detalle de ejercicio por id'),
    path('exercise/category/<int:pk>', ExerciseByCategoryAPIView.as_view(), name="lista de ejercicios por categoria"),

    #get options by idExercise
    path('options/<int:pk>', OptionsByExerciseAPIView.as_view(), name='obtener lista de optiones por id de ejercicio'),
    #get options by idTheme-Learnig
    path('learning/options/<int:pk>',OptionsByThemeAPIView.as_view(), name="lista de optiones por theme"),
    #get student by idCount
    path('student/<int:pk>',StudentByIdAccount.as_view(), name="estudiante por id account"),

]   

"""
    path('exercise/', ExerciseAPIView.as_view(), name = 'lista de exercicios'),
    #get details 
    path('exercise/category/<int:categoryID>/', exercise_by_category, name = 'lista de exercicios por categoria'), 
    path('exercise/<int:pk>', exercise_by_id, name = 'detalle de ejercicio por id'), """
