from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    A signal receiver to create a profile for a new user.

    Args:
        sender: The model class.
        instance: The actual instance being saved.
        created: A boolean that's True if a new record was created.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def set_username(sender, instance, *args, **kwargs):
    """
    A signal receiver to set the username of a user to their email address.

    Args:
        sender: The model class.
        instance: The actual instance being saved.
    """
    if not instance.username:
        username = f'{instance.first_name}_{instance.last_name}'.lower()
        counter = 1
        while User.objects.filter(username=username):
            username = f'{instance.first_name}_{instance.last_name}_{counter}'.lower()
            counter += 1
        instance.username = username
