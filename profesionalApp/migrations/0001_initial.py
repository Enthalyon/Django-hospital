# Generated by Django 4.1.1 on 2022-10-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfesionalMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(default='Sin nombres', max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(default='Sin apellidos', max_length=50, verbose_name='Apellidos')),
                ('telefono', models.CharField(default='Sin telefono', max_length=50, verbose_name='Telefono')),
                ('genero', models.CharField(default='Sin genero', max_length=50, verbose_name='Genero')),
                ('direccion', models.CharField(default='Sin direccion', max_length=50, verbose_name='Direccion')),
                ('especialidad', models.CharField(default='Sin especialidad', max_length=50, verbose_name='Especialidad')),
                ('es_medico', models.BooleanField(default=False, verbose_name='EsMedico')),
            ],
        ),
    ]
