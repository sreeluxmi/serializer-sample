# django
from django.urls import path, include
from rest_framework import routers


# from .views import book_list, book_create, book
# from .views import BookList, Bookdetail
from .views import SeriesViewSet


router = routers.DefaultRouter()
router.register(r'series', SeriesViewSet)
urlpatterns = [
    # path('book-create/', book_create, name="book-create"),
    # path('book-list/', book_list, name="book-list"),
    # path('book/<int:pk>/', book, name="book"),
    # path('book/', BookList.as_view()),
    # path('book/<int:pk>/', Bookdetail.as_view()),

    path('', include(router.urls))

]
