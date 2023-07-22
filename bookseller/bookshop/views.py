from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AuthorUserSerializer, CategorySerializer, BooksSerializer
from .permissions import IsAuthor
from . import models
from .models import Category
from .filter import BookFilter

class AuthorUserView(viewsets.ModelViewSet):
    serializer_class = AuthorUserSerializer
    permision_class = [IsAuthor]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AllBooksView(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
    serializer_class = BooksSerializer
    permission_class = [AllowAny]

    def get_queryset(self):
        return models.Books.objects.all()


class BooksView(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
    serializer_class = BooksSerializer
    permission_class = [IsAuthor]

    def get_queryset(self):
        return models.Books.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
