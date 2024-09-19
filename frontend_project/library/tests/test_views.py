from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from library.models import User, Book


class EnrollUserViewTest(APITestCase):

    def test_enroll_user(self):
        """Test enrolling a user via the API"""
        url = reverse('enroll-user')
        data = {
            "email": "john.doe@example.com",
            "first_name": "John",
            "last_name": "Doe"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "john.doe@example.com")


class ListAvailableBooksViewTest(APITestCase):

    def setUp(self):
        Book.objects.create(
            title="Clean Code",
            author="Robert Martin",
            publisher="Prentice Hall",
            category="Technology"
        )
        Book.objects.create(
            title="The Mythical Man-Month",
            author="Frederick Brooks",
            publisher="Addison-Wesley",
            category="Technology",
            is_borrowed=True  # Borrowed book
        )

    def test_list_available_books(self):
        """Test listing all available books via the API"""
        url = reverse('list-books')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Only 1 available book
        self.assertEqual(response.data[0]['title'], "Clean Code")


class BorrowBookViewTest(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="The Mythical Man-Month",
            author="Frederick Brooks",
            publisher="Addison-Wesley",
            category="Technology",
            is_borrowed=False
        )

    def test_borrow_book(self):
        """Test borrowing a book via the API"""
        url = reverse('borrow-book', kwargs={'id': self.book.id})
        response = self.client.put(url, format='json')
        #print(response.content_type)
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertTrue(self.book.is_borrowed)
