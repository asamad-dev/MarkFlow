from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('documents.urls')),

    # Only serve OpenAPI schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]
