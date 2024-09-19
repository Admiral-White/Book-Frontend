from django.test import TestCase
from library.models import User, Book
#from library.models import Book


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="jane.doe@example.com",
            first_name="Jane",
            last_name="Doe"
        )

    def test_user_creation(self):
        """Test if the user is created successfully"""
        self.assertEqual(self.user.email, "jane.doe@example.com")
        self.assertEqual(self.user.first_name, "Jane")
        self.assertEqual(self.user.last_name, "Doe")

    def test_user_str(self):
        """Test string representation of the user"""
        self.assertEqual(str(self.user), "jane.doe@example.com")


class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="The Pragmatic Programmer",
            author="Andrew Hunt",
            publisher="Addison-Wesley",
            category="Technology"
        )

    def test_book_creation(self):
        """Test if the book is created successfully"""
        self.assertEqual(self.book.title, "The Pragmatic Programmer")
        self.assertEqual(self.book.author, "Andrew Hunt")
        self.assertEqual(self.book.publisher, "Addison-Wesley")
        self.assertEqual(self.book.category, "Technology")

    def test_book_str(self):
        """Test string representation of the book"""
        self.assertEqual(str(self.book), "The Pragmatic Programmer")