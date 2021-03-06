from django.db import models
from django.contrib.auth.models import User
import uuid
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    social_youtube= models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.user.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000, default='describe your experience here on this skill', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


# # signal 

# @receiver(post_save, sender=User)
# def profileUpdated(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         Profile.objects.create(
#             user = user,
#             username = user.username,
#             name = user.first_name,
#             email = user.email,

#         )


# @receiver(post_delete, sender=Profile)
# def deleteUser(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()


# # post_save.connect(profileUpdated, sender=Profile)
# # post_delete.connect(deleteUser, sender=Profile)