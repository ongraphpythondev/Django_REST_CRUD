from CRUD.models import Book
from CRUD.serializers import Book_Serializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Books(APIView):
    """
    List all Books, or create a new Book.
    """
    def get(self, request):
        """It shows all the books.

        Returns:
            dict: All books data.
        """
        Books = Book.objects.all()
        serializer = Book_Serializer(Books, many=True)
        return Response(serializer.data)

    def post(self, request):
        """It create a book.

        Returns:
            dict: Book data that is created.
        """
        serializer = Book_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class Book_class(APIView):
    """
    Retrieve, update or delete a book instance.
    """
    def get(self, request , pk):
        """It show a specific book.

        Args:
            pk (int): This is the primary key of a perticular book

        Returns:
            dict: Single book data.
        """
        book = Book.objects.filter(pk = pk).first()
        if not book:
            return Response({"status":"Book not found"})
        serializer = Book_Serializer(book)
        return Response(serializer.data)

    def put(self, request , pk):
        """It update a specific book.
        
        Args:
            pk (int): This is the primary key of a perticular book

        Returns:
            dict: Updated book data.
        """
        book = Book.objects.filter(pk = pk).first()
        serializer = Book_Serializer(book ,data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , pk):
        """It delete a specific book.
        
        Args:
            pk (int): This is the primary key of a perticular book

        Returns:
            dict: Tell the status that book is deleted.
        """
        book = Book.objects.filter(pk = pk).first()
        response = {"status": f"{book.name} book is deleted"}
        book.delete()
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

