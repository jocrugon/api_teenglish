from email.mime import image
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    android_version = models.CharField(max_length=5)
    birth = models.DateField()
    email = models.EmailField(max_length=50, unique=True)
    create_date = models.DateField(auto_now_add=True)
    dni = models.CharField(max_length=8, unique=True, blank=True, null=True)
    father_lastname = models.CharField(max_length=50, blank=True, null=True)
    genders = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    gender = models.CharField(max_length=1, choices=genders, default='F')
    mother_lastname = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255)
    photo =models.ImageField('Imagen de perfil', upload_to='assets/profile/', default="assets/dfImage.jpg" , blank=True, null=True)
    state = models.SmallIntegerField(default=1)
    current_score = models.IntegerField(default=0)
    def __str__(self):
        return f'id: {self.id} - Account: {self.email} - name: {self.name} {self.father_lastname} {self.mother_lastname}'


class Category(models.Model):
    category = models.CharField(max_length=100)
    state = models.SmallIntegerField(default=1)
    icon_name = models.CharField(max_length=50, blank=True, null=True, default="ban")
    def __str__(self):
        return f'id: {self.id} - Category: {self.category}'


class Type_exercise(models.Model):
    type_exercise = models.CharField(max_length=100)
    state = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'id: {self.id} - Type: {self.type_exercise}'


class Message_motivation(models.Model):
    message = models.TextField(max_length=100)
    state = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'id: {self.id} - Message: {self.message}'


class Exercise(models.Model):
    message_motivation = models.ForeignKey(Message_motivation, on_delete=models.SET_NULL, null=True)
    type_exercise = models.ForeignKey(Type_exercise, on_delete=models.SET_NULL, null=True)
    exercise = models.CharField(max_length=100)
    instruction = models.CharField(max_length=100)
    phrase_translate = models.CharField(max_length=100, blank=True, null = True)
    score = models.IntegerField(default=20)
    state = models.SmallIntegerField(default=1)
    icon_name = models.CharField(max_length=50, blank=True, null=True, default="ban")
    
    def __str__(self):
        return f'id: {self.id} - Exercise: {self.exercise} - Instruction: {self.instruction} - To Translate: {self.phrase_translate} - Score: {self.score}'


class List_exercises_category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return f'category: |{self.category}| - exercise: |{self.exercise}|'


class Option(models.Model):
    option = models.CharField(max_length=30)
    image = models.ImageField('Imagen de la opción', upload_to='assets/exercises/', default="assets/dfImage.jpg", blank=True, null=True)
    state = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'Option: |{self.option}|'


class List_options_exercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True)
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Exercise |{self.exercise}| - Option |{self.option}'

