# Generated by Django 4.1.1 on 2022-10-03 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('familiarAsignadoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(default='Sin nombre', max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(default='Sin apellido', max_length=50, verbose_name='Apellido')),
                ('telefono', models.CharField(default='Sin telefono', max_length=50, verbose_name='Telefono')),
                ('genero', models.CharField(default='Sin genero', max_length=50, verbose_name='Genero')),
                ('direccion', models.CharField(default='Sin direccion', max_length=50, verbose_name='Direccion')),
                ('ciudad', models.CharField(default='Sin ciudad', max_length=50, verbose_name='Ciudad')),
                ('fecha_de_nacimiento', models.DateTimeField(default='Sin fecha de nacimiento', verbose_name='FechaDeNacimiento')),
                ('id_familiar_asignado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='familiarAsignadoApp.familiarasignado')),
            ],
        ),
    ]
