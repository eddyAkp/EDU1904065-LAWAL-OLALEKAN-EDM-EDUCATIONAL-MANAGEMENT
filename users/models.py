from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

LIBRARY_POSITION_CHOICES = (
    ('Chief Librarian', 'Chief Librarian'),
    ('Head of Acquisitions', 'Head of Acquisitions')
)


class AuthorizedUser(AbstractUser):
    """Custom user model class"""
    pass
