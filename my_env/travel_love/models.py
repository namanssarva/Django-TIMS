from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Travel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null = True, blank = True)
    place_name = models.CharField(max_length=100)
    place_description = models.TextField()
    place_image = models.ImageField(upload_to="images")