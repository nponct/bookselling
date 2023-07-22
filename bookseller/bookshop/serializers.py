from rest_framework import serializers
from .import models


class AuthorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Authors
        fields=('user','full_name','city','country','personnel_data')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields=('name',)

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Books
        fields=('user','title','content','description','page_number','cover','cats','publ_date','placed_date')