from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import  TasksSerializer
from .permissions import IsAuthor
from . import models
from .filter import TaskFilter
from.models import Tasks
from.tasks import send_mail_func


class AllTasksView(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
    serializer_class = TasksSerializer
    permission_class = [AllowAny]

    def get_queryset(self):
        return models.Tasks.objects.all()


class TasksView(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
    serializer_class = TasksSerializer
    permission_class = [IsAuthor]

    def get_queryset(self):
        return models.Tasks.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def send_alarm_to_user(self,request):
        send_mail_func.delay(self.request.user.email)
        return HttpResponse ('Email has been sent successfully')

    # def get_queryset(self):
    # return models.Tasks.objects.filter(user=self.request.user,datecompleted__gte=datetime.date())








