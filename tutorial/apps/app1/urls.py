# django
from django.urls import path


from .views import book_list, book_create, book

urlpatterns = [
    path('book-create/', book_create, name="book-create"),
    path('book-list/', book_list, name="book-list"),
    path('book/<int:pk>/', book, name="book"),

]
