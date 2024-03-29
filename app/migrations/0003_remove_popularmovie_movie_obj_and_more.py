# Generated by Django 4.1.5 on 2023-01-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_popularmovie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularmovie',
            name='movie_obj',
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='contentRating',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='countries',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='fullTitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='genres',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='image',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='keywords',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='languages',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='movie_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='plot',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='ratings',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='releaseDate',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='runtimeStr',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='similars',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='stars',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='popularmovie',
            name='trailer',
            field=models.JSONField(default=dict),
        ),
    ]
