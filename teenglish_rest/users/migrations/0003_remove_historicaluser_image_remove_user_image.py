# Generated by Django 4.0.3 on 2022-04-10 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaluser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]