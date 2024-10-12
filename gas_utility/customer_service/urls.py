from django.urls import path
from . import views  # Ensure you're importing views correctly

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),  # This should match the view name
    path('status/', views.request_status, name='request_status'),  # Ensure this matches the view name
]