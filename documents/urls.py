from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, login_user

router = DefaultRouter()
router.register('documents', DocumentViewSet, basename='documents')

urlpatterns = [
    path('users/<int:id>/login/', login_user, name='login'),
    path('', include(router.urls)),
]
