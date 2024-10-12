from django.contrib import admin
from django.urls import path, include
from customer_service import views  # Import the view you want to use for the root URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('customer_service.urls')),
    path('', views.submit_request, name='home'),  # Define a root URL pattern here
]

# Serving media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from customer_service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('customer_service.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line for auth views
    path('', views.submit_request, name='home'),
]