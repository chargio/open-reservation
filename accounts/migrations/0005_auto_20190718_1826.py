# Generated by Django 2.2.3 on 2019-07-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190717_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='father_name',
            field=models.CharField(default='padre', max_length=150, verbose_name='nombre completo del padre'),
        ),
        migrations.AddField(
            model_name='user',
            name='mother_name',
            field=models.CharField(default='madre', max_length=150, verbose_name='nombre completo de la madre'),
        ),
    ]
