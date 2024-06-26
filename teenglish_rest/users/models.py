from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, name,last_name_p ,last_name_m, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            name = name,
            last_name_p = last_name_p,
            last_name_m = last_name_m,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, name,last_name_p, last_name_m, password=None, **extra_fields):
        return self._create_user(username, name,last_name_p, last_name_m, password, False, False, **extra_fields)

    def create_superuser(self, username, name,last_name_p, last_name_m, password=None, **extra_fields):
        return self._create_user(username, name,last_name_p, last_name_m, password, True, True, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name_p = models.CharField('Apellido Paterno', max_length = 255, blank = True, null = True)
    last_name_m = models.CharField('Apellido Materno', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','last_name_p','last_name_m']

    def __str__(self):
        return f'{self.name} {self.last_name_p} {self.last_name_m}'