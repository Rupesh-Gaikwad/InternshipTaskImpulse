from django.shortcuts import render
from rest_framework.serializers import Serializer
from taskApp.models import StudentTask
from taskApp.serializers import ListAllTasksSerializer, StudentTaskInputSerializer 
from rest_framework.generics import CreateAPIView, ListAPIView

# Create your views here.

class ListStudentsTaskView(ListAPIView):
    queryset = StudentTask.objects.all()
    serializer_class = ListAllTasksSerializer

class AddNewTaskView(CreateAPIView):
    queryset = StudentTask
    serializer_class = StudentTaskInputSerializer
