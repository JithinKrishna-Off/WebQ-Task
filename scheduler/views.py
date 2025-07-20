from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Welcome to the Welcome Call Backend!'})


# Create your views here.
from rest_framework import viewsets
from .models import CallSchedule, CallNotes
from .serializers import CallScheduleSerializer, CallNotesSerializer

class CallScheduleViewSet(viewsets.ModelViewSet):
    queryset = CallSchedule.objects.all().order_by('-call_datetime')
    serializer_class = CallScheduleSerializer

class CallNotesViewSet(viewsets.ModelViewSet):
    queryset = CallNotes.objects.all().order_by('-created_at')
    serializer_class = CallNotesSerializer
