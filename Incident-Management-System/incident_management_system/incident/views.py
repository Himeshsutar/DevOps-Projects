from rest_framework import viewsets
from .models import Incident
from .serializers import IncidentSerializer
from django.core.mail import send_mail

def send_incident_notification(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        'your_email@gmail.com',  # Make sure this matches your email settings
        [recipient_email],
        fail_silently=False,
    )

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def perform_create(self, serializer):
        incident = serializer.save(created_by=self.request.user)
        if incident.assigned_to:
            send_incident_notification(
                "New Incident Assigned",
                f"You have been assigned to: {incident.title}",
                incident.assigned_to.email
            )

    def perform_update(self, serializer):
        incident = serializer.save()
        if incident.status == 'resolved' and incident.assigned_to:
            send_incident_notification(
                "Incident Resolved",
                f"The incident '{incident.title}' has been resolved.",
                incident.created_by.email
            )

    
