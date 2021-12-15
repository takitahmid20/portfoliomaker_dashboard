from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True)
    #-----------HOME PAGE--------------
    profile_image = models.ImageField(null=True, blank=True, upload_to='media/')
    name = models.CharField(max_length=40)
    short_introduction = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    twitter = models.CharField(max_length=500, blank=True)
    instagram = models.CharField(max_length=500, blank=True)
    linkedin = models.CharField(max_length=500, blank=True)
    #-----------ABOUT PAGE--------------
    about_banner_img = models.ImageField(null=True, blank=True, upload_to='media/')
    bio = models.TextField(max_length=200, blank=True)
    birthday = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=15)
    study_in = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)


class videoModel(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    video_title = models.CharField(max_length=200, null=True, blank=True)
    video_link = models.CharField(max_length=500, null=True, blank=True)
    video_thumbnail = models.ImageField(blank=True, upload_to='media/')

    def __str__(self):
        return str(self.video_title)


class imageModel(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    image_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='media/')

    def __str__(self):
        return str(self.image_title)


class projectModel(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    project_name = models.CharField(max_length=200, null=True, blank=True)
    project_feature_image = models.ImageField(blank=True, upload_to='media/')
    project_details = models.TextField(max_length=200, blank=True)
    project_client = models.CharField(max_length=200, null=True, blank=True)
    project_category = models.CharField(max_length=200, null=True, blank=True)
    project_completed_year = models.IntegerField(null=True, blank=True)
    project_img_2 = models.ImageField(blank=True, upload_to='media/')
    project_img_3 = models.ImageField(blank=True, upload_to='media/')
    project_img_4 = models.ImageField(blank=True, upload_to='media/')

    def __str__(self):
        return str(self.project_name)