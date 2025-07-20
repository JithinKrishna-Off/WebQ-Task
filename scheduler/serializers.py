from rest_framework import serializers
from .models import CallSchedule, CallNotes

class CallScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallSchedule
        fields = '__all__'

class CallNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallNotes
        fields = '__all__'
