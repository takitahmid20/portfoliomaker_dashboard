from django.db import models
from django.contrib.auth.models import User
import uuid


WHO_ARE_YOU = (
    ('influencer','Influencer'),
    ('content_creator', 'Content Creator'),
    ('youtuber','Youtuber'),
    ('web_developer','Web Developer'),
    ('graphics_designer','Graphics Designer'),
    ('teacher','Teacher'),
    ('student','Student'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True)
    #-----------HOME PAGE--------------
    profile_image = models.ImageField(null=True, blank=True, upload_to='media/')
    name = models.CharField(max_length=40)
    who_are_you = models.CharField(max_length=30, choices=WHO_ARE_YOU, default='influencer')
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
    
    @property
    def image_url(self):
        if self.video_thumbnail and hasattr(self.video_thumbnail, 'url'):
            return self.video_thumbnail.url


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
    project_details = models.TextField(blank=True)
    project_client = models.CharField(max_length=200, null=True, blank=True)
    project_category = models.CharField(max_length=200, null=True, blank=True)
    project_completed_year = models.IntegerField(null=True, blank=True)
    project_img_2 = models.ImageField(blank=True, upload_to='media/')
    project_img_3 = models.ImageField(blank=True, upload_to='media/')
    project_img_4 = models.ImageField(blank=True, upload_to='media/')

    def __str__(self):
        return str(self.project_name)


class mySkills(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    skill_name = models.CharField(max_length=200,null=True, blank=True)
    skill_percentage = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.skill_name)


class languageSkills(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    language_name = models.CharField(max_length=200, null=True, blank=True)
    language_percentage = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.language_name)


class extras(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    total_completed_projects = models.IntegerField(null=True, blank=True)
    total_clients = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.total_completed_projects)


class blogModel(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    blog_title = models.CharField(max_length=200, blank=True, null=True)
    blog_description = models.TextField(blank=True, null=True)
    blog_thumbnail = models.ImageField(blank=True, null=True)
    blog_category = models.CharField(blank=True, null=True, max_length=50)
    blog_tags = models.CharField(max_length=200, blank=True, null=True)
    blog_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.blog_title)