# django
from django.urls import path


# from .views import book_list, book_create, book
from .views import BookList, BookCreate, Bookdetail

urlpatterns = [
    # path('book-create/', book_create, name="book-create"),
    # path('book-list/', book_list, name="book-list"),
    # path('book/<int:pk>/', book, name="book"),
    path('book-list/', BookList.as_view()),
    path('book-create/', BookCreate.as_view()),
    path('book-detail/<int:pk>/', Bookdetail.as_view())

]
