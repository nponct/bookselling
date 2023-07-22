from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    nick_name = models.CharField(max_length=30, blank=True, null=True)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.nick_name or ''


class Tasks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, )
    title = models.CharField(max_length=100, verbose_name="Название задания")
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    datecompleted = models.DateTimeField(null=True, verbose_name="Время выполнения")
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title or ''
