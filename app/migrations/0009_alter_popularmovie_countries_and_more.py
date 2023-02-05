# Generated by Django 4.1.5 on 2023-02-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_popularmovie_streamingservices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularmovie',
            name='countries',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='genres',
            field=models.CharField(default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='keywords',
            field=models.CharField(default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='languages',
            field=models.CharField(default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='plot',
            field=models.CharField(default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='ratings',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='releaseDate',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='runtimeStr',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='similars',
            field=models.CharField(default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='stars',
            field=models.CharField(default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='trailer',
            field=models.JSONField(default=dict, null=True),
        ),
    ]