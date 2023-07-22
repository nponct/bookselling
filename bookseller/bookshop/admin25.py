from django.contrib import admin
from .import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .models import Users

@admin.register(models.Users)
class UsersAdmin(UserAdmin):

    model = Users

    add_fieldsets=(
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields':(
                    'is_author',
                    'nick_name',
                )
            }
        )
    )
    fieldsets=(
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields':(
                    'is_author',
                    'nick_name',

                )
            }
        )
    )




@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display=('id','title','user','create','datecompleted','memo','important')
    list_display_links=('title',)


