# Generated by Django 4.1.5 on 2023-02-07 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_profile_fname_profile_lname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularmovie',
            name='trailer',
        ),
    ]
