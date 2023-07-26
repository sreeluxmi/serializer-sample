from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, viewsets

# Create your views here.

from .models import Series
from .serializer import SeriesSerializer


from rest_framework.pagination import PageNumberPagination


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response({
#             'error': 'Book does not exist'
#         }, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#              status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "DELETE":
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.views import APIView


# class BookList(APIView):

#     def get(self, request):
#         paginator = PageNumberPagination()
#         paginator.page_size = 5

#         books = Series.objects.all()
#         paginated_books = paginator.paginate_queryset(books, request)

#         serializer = SeriesSerializer(paginated_books, many=True)
#         return paginator.get_paginated_response(serializer.data)
 
#     def post(self, request):
#         serializer = SeriesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class Bookdetail(APIView):

#     def get_book_by_pk(self, pk):
#         try:
#             return Series.objects.get(pk=pk)
#         except Series.DoesNotExist:
#             return Response({
#                 'error': 'Book does not exist'
#             }, status=status.HTTP_404_NOT_FOUND)
 
#     def get(self, request, pk):
#         book = self.get_book_by_pk(pk)
#         serializer = SeriesSerializer(book)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         book = self.get_book_by_pk(pk)
#         serializer = SeriesSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         book = self.get_book_by_pk(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)