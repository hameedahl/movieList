from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() # get the currently logged in user
# Create your models here.

# Table with each row
class Profile(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        id_user = models.IntegerField()
        bio = models.TextField(blank=True) # blank b/c this option is optional
        profile_img = models.ImageField(upload_to='profile_images',default='') # place default in media dir
        location = models.CharField(max_length=100, blank=True)

        def __str__(self) -> str:
                return self.user.username


class PopularMovie(models.Model):
    fullTitle = models.CharField(max_length=100, default='')
    movie_id = models.CharField(max_length=50, default='')
    image = models.CharField(max_length=100, default='')
    releaseDate = models.CharField(max_length=20, default='')
    runtimeStr = models.CharField(max_length=20, default='')
    plot = models.CharField(max_length=10000, default='')
    stars = models.CharField(max_length=10000, default='')
    genres = models.CharField(max_length=10000, default='')
    countries = models.CharField(max_length=1000, default='')
    languages = models.CharField(max_length=10000, default='')
    contentRating = models.CharField(max_length=10, default='', null=True)
    ratings = models.JSONField(default=dict)
    trailer = models.JSONField(default=dict)
    keywords = models.CharField(max_length=10000, default='')
    similars = models.CharField(max_length=10000, default='')
    # streamingServices = models.JSONField(default=dict)


    def __str__(self):
        return self.fullTitle