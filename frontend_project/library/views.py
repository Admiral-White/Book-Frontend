from rest_framework import generics
from .models import User, Book
from .serializers import UserSerializer, BookSerializer


# Enroll users
class EnrollUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# List available books
class ListAvailableBooksView(generics.ListAPIView):
    queryset = Book.objects.filter(is_borrowed=False)  # Only list available books
    serializer_class = BookSerializer


# Borrow a book
class BorrowBookView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(is_borrowed=True)
