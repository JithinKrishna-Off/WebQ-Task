from django.db import models
from django.contrib.auth.models import User

class CallSchedule(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    call_datetime = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_calls')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'call_datetime'], name='unique_call_schedule')
        ]

class CallNotes(models.Model):
    schedule = models.ForeignKey(CallSchedule, on_delete=models.CASCADE)
    raw_notes = models.TextField()
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
