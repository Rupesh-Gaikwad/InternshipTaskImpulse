from rest_framework import serializers
from taskApp.models import StudentTask

class ListAllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTask
        fields = '__all__'

class StudentTaskInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTask
        fields = ('name', 'description', 'email')