from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
      <title>Incident Management System</title>
      <style>
        body {
          background-color: yellow;
          color: #333;
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          margin: 0;
          height: 100vh;
        }

        h1 {
          font-size: 3rem;
          color: #0056b3;
          text-align: center;
          margin-top: 20px;
        }

        p {
          text-align: center;
          font-size: 1.2rem;
          margin-top: 10px;
          color: #444;
        }

        a {
          color: #d9534f; /* Bootstrap's red-like color */
          text-decoration: none;
          font-weight: bold;
        }

        a:hover {
          text-decoration: underline;
        }
      </style>
    </head>
    <body>
      <h1>Welcome to the Incident Management System!</h1>
      <p>Go to <a href="/admin/">admin page</a> and check for incidents.</p>
    </body>
    </html>
    """)

urlpatterns = [
    path('', home),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include('incident_management_system.incident.urls')),
    path('api-auth/', include('rest_framework.urls')),  # For login/logout in browsable API
]
