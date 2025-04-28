
from django.db import models
from django.contrib.auth.models import User

class Incident(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_incidents')
    assigned_to = models.ForeignKey(
    User, 
    on_delete=models.SET_NULL,  # If the user is deleted, set the field to NULL
    null=True,                  # Allow the field to be NULL in the database
    blank=True,                 # Allow the field to be blank in forms
    related_name='assigned_incidents'  # Reverse relationship: allows querying from User to Incident
)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
