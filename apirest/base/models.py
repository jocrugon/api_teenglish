from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado',default = True)
    

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'