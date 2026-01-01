from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_user_to_normal_group(sender, instance, created, **kwargs):
    if created:
        normal_group = Group.objects.get(name='Normal User')
        instance.groups.add(normal_group)