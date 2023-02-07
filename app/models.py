from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
User = get_user_model() # get the currently logged in user
# Create your models here.

# Table with each row
class Profile(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        fname = models.CharField(max_length=100, blank=False, default='')
        lname = models.CharField(max_length=100, blank=True, default='')
        id_user = models.IntegerField()
        bio = models.TextField(blank=True) # blank b/c this option is optional
        profile_img = models.ImageField(upload_to='profile_images',default='') # place default in media dir
        location = models.CharField(max_length=100, blank=True)

        def __str__(self) -> str:
                return self.user.username


class PopularMovie(models.Model):
    fullTitle = models.CharField(max_length=100, default='', null=True)
    movie_id = models.CharField(max_length=50, default='', null=True)
    image = models.CharField(max_length=100, default='', null=True)
    releaseDate = models.CharField(max_length=20, default='', null=True)
    runtimeStr = models.CharField(max_length=20, default='', null=True)
    plot = models.CharField(max_length=10000, default='', null=True)
    stars = models.CharField(max_length=10000, default='' , null=True)
    genres = models.CharField(max_length=10000, default='', null=True)
    countries = models.CharField(max_length=1000, default='', null=True)
    languages = models.CharField(max_length=10000, default='', null=True)
    contentRating = models.CharField(max_length=10, default='', null=True)
    ratings = models.JSONField(default=dict, null=True)
    keywords = models.CharField(max_length=10000, default='', null=True)
    similars = models.CharField(max_length=10000, default='', null=True)

    def __str__(self) -> str:
        return str(self.fullTitle)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4) 
    user = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100)
    movie_img_url = models.CharField(max_length=500, default='')
    movie_title = models.CharField(max_length=100)
    caption = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)
    num_likes = models.IntegerField(default=0)

    def __str__(self) -> str:
          return self.user
