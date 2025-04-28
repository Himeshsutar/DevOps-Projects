from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def home(request):
    return HttpResponse("Welcome to the Incident Management System!")

urlpatterns = [
    path('', home),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include('incident_management_system.incident.urls')),
    path('api-auth/', include('rest_framework.urls')),  # For login/logout in browsable API
]
