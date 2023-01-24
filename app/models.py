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