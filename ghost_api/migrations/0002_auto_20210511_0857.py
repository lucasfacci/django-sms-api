# Generated by Django 3.1.5 on 2021-05-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghost_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]