from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)  # default value is False
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add=True means that the field will be automatically set to now when the object is first created

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
    details = models.TextField(blank=True)     # Additional information
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = self.user.username if self.user else "System/Anonymous"
        return f"{self.timestamp} | {username} | {self.action}"

    class Meta:
        ordering = ['-timestamp']              # Newest first
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'