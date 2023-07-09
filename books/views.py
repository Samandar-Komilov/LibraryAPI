from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# Jarayon
class BookListApiView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializers_data = BookSerializer(books, many=True).data
        data = {
            "status":f"Returned {len(books)} books",
            "books":serializers_data,
        }

        return Response(data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                'book':serializer_data,
                'status':'Success!'
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
            {"status":"False",
             "message":"Book is not found"}, status=status.HTTP_404_NOT_FOUND,
        )
        
# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        # We used get_object_or_404 instead of try/except here.
        book = get_object_or_404(id=pk)
        book.delete()
        return Response({"status":True,"message":"Successfully deleted!"})


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {'status':True,
             'message':f'Book {book_saved} is updated successfully!'}
        )

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# Jarayon
class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status':f'Books are saved to the database!',
                'books':data,
            }
            return Response(data)

# Double Generic Views
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer