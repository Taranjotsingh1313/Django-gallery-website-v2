from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)
class image(models.Model):
    img_title = models.CharField(max_length=50)
    img_desc = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='imagebazaar')
    # img_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img_user = models.ForeignKey(User,on_delete=models.CASCADE)