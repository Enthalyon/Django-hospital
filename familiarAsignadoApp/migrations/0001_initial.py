# Generated by Django 4.1.1 on 2022-10-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliarAsignado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(default='Sin nombre', max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(default='Sin apellido', max_length=50, verbose_name='Apellido')),
                ('telefono', models.CharField(default='Sin telefono', max_length=50, verbose_name='Telefono')),
                ('genero', models.CharField(default='Sin genero', max_length=50, verbose_name='Genero')),
                ('direccion', models.CharField(default='Sin direccion', max_length=50, verbose_name='Direccion')),
                ('parentesco', models.CharField(default='Sin parentesco', max_length=50, verbose_name='Parentesco')),
            ],
        ),
    ]
