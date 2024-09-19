from django.db import models


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    is_borrowed = models.BooleanField(default=False)  # Tracks whether the book is borrowed

    def __str__(self):
        return self.title
