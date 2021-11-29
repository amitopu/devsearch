from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

# signal 

@receiver(post_save, sender=User)
def profileUpdated(sender, instance, created, **kwargs):
    print('User is triggered')
    if created:
        user = instance
        Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            email = user.email,

        )


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)