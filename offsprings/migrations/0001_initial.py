# Generated by Django 2.2.3 on 2019-07-08 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offspring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=75, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=150, verbose_name='apellidos')),
                ('grade', models.IntegerField(choices=[(1, 'Primero de Primaria'), (2, 'Segundo de Primaria'), (3, 'Tercero de Primaria'), (0, 'Otros')], default=1, verbose_name='curso')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='padre o tutor')),
            ],
        ),
    ]