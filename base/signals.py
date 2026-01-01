from django.contrib.auth.models import User, Group
from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Task, AuditLog


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', 'Unknown')
    return ip


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

# Successful login logging
@receiver(user_logged_in)
def log_user_login(sender, user, request, **kwargs):
    ip = get_client_ip(request)
    AuditLog.objects.create(
        user=user,
        action="LOGIN_SUCCESS",
        details=f"User logged in from IP: {ip}"
    )


# Failed login logging
@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    username = credentials.get('username', '<unknown>')
    ip = get_client_ip(request)
    AuditLog.objects.create(
        user=None,  # User unknown because login failed
        action="LOGIN_FAILED",
        details=f"Failed login attempt for username '{username}' from IP: {ip}"
    )


# Logout logging
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    AuditLog.objects.create(
        user=user,
        action="LOGOUT",
        details=f"User logged out from IP: {ip}"
    )


# Log Task create and update
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


# Log Task delete
@receiver(post_delete, sender=Task)
def log_task_delete(sender, instance, **kwargs):
    AuditLog.objects.create(
        user=instance.user,
        action="TASK_DELETE",
        details=f"Deleted task: '{instance.title}'"
    )
