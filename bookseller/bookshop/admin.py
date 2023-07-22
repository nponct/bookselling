from django.contrib import admin
from .import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UsersCreationForm,UsersChangeForm
from .models import Users

@admin.register(models.Users)
class UsersAdmin(UserAdmin):
    #add_form = UsersCreationForm
    #form = UsersChangeForm
    model = Users
    #list_display = ('username','first_name','last_name','email','is_staff','is_active','date_joined','nick_name', 'is_author')
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

@admin.register(models.Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display=('id','email','full_name','join_date')
    list_display_links=('full_name',)


@admin.register(models.Books)
class BooksAdmin(admin.ModelAdmin):
    list_display=('id','title','user','publ_date')
    list_display_links=('title',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    list_display_links=('name',)

