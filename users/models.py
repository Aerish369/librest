from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LIBRARIAN = 'librarian'
    MEMBER = 'member'
    GUEST = 'guest'

    ROLE_CHOICES = [
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
        (GUEST, 'Guest')
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=MEMBER)

    def __str__(self) -> str:
        return self.username