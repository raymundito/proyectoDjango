# Generated by Django 4.2 on 2023-05-04 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='password',
            new_name='contrasenia',
        ),
    ]