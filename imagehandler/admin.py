from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','img_title','img_desc')