from django.contrib import admin
from django.urls import path, include
from scheduler import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('scheduler.api_urls')),  # All your API routes
    path('', views.home, name='home'),            # Home view (optional)
]
