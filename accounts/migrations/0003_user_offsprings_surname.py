# Generated by Django 2.2.3 on 2019-07-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='offsprings_surname',
            field=models.CharField(max_length=150, null=True, verbose_name='apellidos de los catecúmenos'),
        ),
    ]