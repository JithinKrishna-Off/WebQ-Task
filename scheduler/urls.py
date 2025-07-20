from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CallScheduleViewSet, CallNotesViewSet

router = DefaultRouter()
router.register(r'calls', CallScheduleViewSet)
router.register(r'notes', CallNotesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
