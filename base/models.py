from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)  # default value is False
<<<<<<< HEAD
    created = models.DateTimeField(auto_now_add=True)  # auto set when created
=======
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add=True means that the field will be automatically set to now when the object is first created
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


# ========================
# AUDIT LOG MODEL (NEW)
# ========================
class AuditLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='audit_logs'
    )
    action = models.CharField(max_length=100)  # e.g., LOGIN, TASK_CREATE, TASK_UPDATE, TASK_DELETE
<<<<<<< HEAD
    details = models.TextField(blank=True)     # Additional information about the action
=======
    details = models.TextField(blank=True)     # Additional information
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = self.user.username if self.user else "System/Anonymous"
        return f"{self.timestamp} | {username} | {self.action}"

    class Meta:
<<<<<<< HEAD
        ordering = ['-timestamp']  # Newest logs first
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
=======
        ordering = ['-timestamp']              # Newest first
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
