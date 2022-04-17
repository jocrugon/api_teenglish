from django.urls import path
from apiBackend.api.views.general_views import *
from apiBackend.api.views.exercise_views import  ExerciseRetrieveAPIView, ExerciseByCategoryAPIView

urlpatterns = [
    #get list
    path('category/', CategoryAPIView.as_view(), name = 'category'),
    path('learning/', LearningAPIView.as_view(), name = 'lista de themes in Learning'),
    
    #get details 
    path('exercise/<int:pk>', ExerciseRetrieveAPIView.as_view(), name = 'detalle de ejercicio por id'),
    path('exercise/category/<int:pk>', ExerciseByCategoryAPIView.as_view(), name="lista de ejercicios por categoria"),

    #get options by idTheme-Learnig
    path('learning/options/<int:pk>',OptionsByThemeAPIView.as_view(), name="lista de optiones por theme"),
    #get student by idCount and update
    path('student/<int:pk>',StudentByIdAccount.as_view(), name="estudiante por id account y permite update"),

    

]   

