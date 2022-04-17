from tabnanny import verbose
from django.db import models

from users.models import User
from base.models import BaseModel

# Create your models here.
class Student(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    genders = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    gender = models.CharField(max_length=1, choices=genders, default='F')
    avatar = models.CharField(max_length=15, default=" ")
    current_score = models.IntegerField(default=0)
    
    class Meta:

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f'id: {self.id} - User: {self.user}'


class Category(BaseModel):
    category = models.CharField(max_length=100)
    
    icon_name = models.CharField(max_length=50, blank=True, null=True, default="ban")
        
    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f'id: {self.id} - Category: {self.category}'


class Type_exercise(BaseModel):
    type_exercise = models.CharField(max_length=100)
    
        
    class Meta:

        verbose_name = 'Type_exercise'
        verbose_name_plural = 'Type_exercises'
    
    def __str__(self):
        return f'id: {self.id} - Type: {self.type_exercise}'


class Message_motivation(BaseModel):
    message = models.CharField(max_length=100)
    
        
    class Meta:

        verbose_name = 'Message_motivation'
        verbose_name_plural = 'Message_motivations'
    
    def __str__(self):
        return f'id: {self.id} - Message: {self.message}'


class Exercise(BaseModel):
    message_motivation = models.ForeignKey(Message_motivation, on_delete=models.SET_NULL, null=True)
    type_exercise = models.ForeignKey(Type_exercise, on_delete=models.SET_NULL, null=True)
    exercise = models.CharField(max_length=100)
    instruction = models.CharField(max_length=100)
    phrase_translate = models.CharField(max_length=100, blank=True, null = True)
    score = models.IntegerField(default=20)
    icon_name = models.CharField(max_length=50, blank=True, null=True, default="ban")
            
    class Meta:

        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'
    
    def __str__(self):
        return f'id: {self.id} - Exercise: {self.exercise} - Instruction: {self.instruction} - To Translate: {self.phrase_translate} - Score: {self.score}'


class List_exercises_category(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null = True)
        
    class Meta:

        verbose_name = 'List_exercises_category'
        verbose_name_plural = 'List_exercises_categories'
    
    def __str__(self):
        return f'category: |{self.category}| - exercise: |{self.exercise}|'


class Option(BaseModel):
    option = models.CharField(max_length=30)
    image = models.ImageField('Imagen de la opción', upload_to='images/exercises/', default="assets/dfImage.jpg", blank=True, null=True)
    is_correct = models.BooleanField(default=False)
        
    class Meta:

        verbose_name = 'Option'
        verbose_name_plural = 'Options'
    
    def __str__(self):
        return f'Option: |{self.option}|'


class List_options_exercise(BaseModel):
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True)
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)
        
    class Meta:

        verbose_name = 'List_options_exercise'
        verbose_name_plural = 'List_options_exercises'
    
    def __str__(self):
        return f'Exercise |{self.exercise}| - Option |{self.option}'


class Learning(BaseModel):
    image = models.ImageField('Image del theme', upload_to='images/learning/', default='assets/dfImage.jpg', blank=True, null=True)
    theme = models.CharField(max_length=20)
        
    class Meta:

        verbose_name = 'Learning'
        verbose_name_plural = 'Learnings'
    
    def __str__(self):
        return f'Theme |{self.theme}|'

class List_options_learning(BaseModel):
    learning = models.ForeignKey(Learning, on_delete=models.SET_NULL, null=True)
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)
        
    class Meta:

        verbose_name = 'List_options_learning'
        verbose_name_plural = 'List_options_learnings'
    
    def __srt__(self):
        return f'Theme: |{self.learning}| - Option: |{self.option}|'
