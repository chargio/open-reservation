# Generated by Django 2.2.3 on 2019-07-17 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
        ('offsprings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offspring',
            name='assignment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedules.Schedule', verbose_name='turno'),
        ),
    ]
