from django.contrib.auth.models import User, Group
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Task, AuditLog


# === RBAC: Auto-add new users to "Normal User" group ===
@receiver(post_save, sender=User)
def add_user_to_normal_group(sender, instance, created, **kwargs):
    if created:
        try:
            normal_group = Group.objects.get(name='Normal User')
            instance.groups.add(normal_group)
        except Group.DoesNotExist:
            pass  # Group not created yet


# === AUDIT LOGGING ===

@receiver(user_logged_in)
def log_user_login(sender, user, request, **kwargs):
    AuditLog.objects.create(
        user=user,
        action="LOGIN",
        details=f"Logged in from IP: {request.META.get('REMOTE_ADDR', 'Unknown')}"
    )


@receiver(post_save, sender=Task)
def log_task_create_update(sender, instance, created, **kwargs):
    if created:
        action = "TASK_CREATE"
        details = f"Created task: '{instance.title}'"
    else:
        action = "TASK_UPDATE"
        details = f"Updated task: '{instance.title}'"
    
    AuditLog.objects.create(
        user=instance.user,
        action=action,
        details=details
    )


@receiver(post_delete, sender=Task)
def log_task_delete(sender, instance, **kwargs):
    AuditLog.objects.create(
        user=instance.user,
        action="TASK_DELETE",
        details=f"Deleted task: '{instance.title}'"
    )