# Generated by Django 4.1.1 on 2022-10-03 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacienteApp', '0001_initial'),
        ('profesionalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='id_profesional_medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profesionalApp.profesionalmedico'),
        ),
    ]