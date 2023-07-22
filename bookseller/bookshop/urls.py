from django.urls import path
from .views import AuthorUserView,CategoryView,BooksView
from .import views



urlpatterns=[
    path('author/',views.AuthorUserView.as_view({'get':'list','post':'create'})),
    path('author/<int:pk>/',views.AuthorUserView.as_view({'put':'update','delete':'destroy'})),
    path('category/',views.CategoryView.as_view({'get':'list','post':'create'})),
    path('books/',views.BooksView.as_view({'get':'list','post':'create'})),
    path('books/<int:pk>/',views.BooksView.as_view({'put':'update','delete':'destroy'})),
]