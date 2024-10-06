from django.contrib import admin  # Import the admin module
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Your existing urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Correctly use 'admin' here
    path('', include('app.urls')),  # Include your app's URLs
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
