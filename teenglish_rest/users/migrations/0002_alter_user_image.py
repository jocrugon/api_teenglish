# Generated by Django 4.0.3 on 2022-04-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='assets/perfil/', verbose_name='Imagen de perfil'),
        ),
    ]