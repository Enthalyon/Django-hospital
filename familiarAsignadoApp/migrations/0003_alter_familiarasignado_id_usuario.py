# Generated by Django 4.1.1 on 2022-10-03 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('familiarAsignadoApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiarasignado',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
