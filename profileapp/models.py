from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    skills = models.CharField(max_length=200, blank=True)
    contact_details = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title