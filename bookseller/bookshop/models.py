from django.db import models
from django.contrib.auth.models import AbstractUser
from .service import get_path_upload_cover,get_path_upload_content


class Users(AbstractUser):
    nick_name = models.CharField(max_length=30, blank=True, null=True)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.nick_name or ''

class Authors(models.Model):
    full_name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    personnel_data = models.TextField(max_length=2000, blank=True, null=True)



    def __str__(self):
        return self.full_name or ''

class Category(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name

class Books(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    cover = models.ImageField(upload_to=get_path_upload_cover)
    content = models.FileField(upload_to=get_path_upload_content)
    publ_date = models.DateTimeField(auto_now_add=True)
    placed_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    page_number = models.PositiveIntegerField()
    cats = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name="category")

    def __str__(self):
        return self.title or ''







