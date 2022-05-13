from django.urls import path
from teenglish.api.views.general_views import *
from teenglish.api.views.exercise_views import  ExerciseRetrieveAPIView,UpdateDetailExerciseByStudentAPIView, ExerciseByCategoryAPIView

urlpatterns = [
    #get list
    path('category/', CategoryAPIView.as_view(), name = 'category'),
    path('learning/', LearningAPIView.as_view(), name = 'lista de themes in Learning'),
    
    #get details 
    path('exercise/<int:pk>', ExerciseRetrieveAPIView.as_view(), name = 'detalle de ejercicio por id'),
    path('exercise/category/<int:idStudent>/<int:idCategory>', ExerciseByCategoryAPIView.as_view(), name="lista de ejercicios por categoria"),

    #get options by idTheme-Learnig
    path('learning/options/<int:pk>',OptionsByThemeAPIView.as_view(), name="lista de optiones por theme"),
    #get student by idCount 
    path('student/<int:idAccount>',StudentByIdAccount.as_view(), name="estudiante por id account"),
    path('student/update/<int:pk>',UpdateScoreInStudent.as_view(), name="update nota del studiante"),

    #update detailsExerciseByStudent&Category
    path('exercise/detail/update/<int:pk>', UpdateDetailExerciseByStudentAPIView.as_view(),name="update de detalle de ejercicio resulto"),

]   

