# bookshelf/models.py
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_create", "Can create a book"),
            ("can_delete", "Can delete a book"),
        ]



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)
    


class CustomUser(AbstractUser):
    # Add additional fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Link the manager to the model
    objects = CustomUserManager()

    def __str__(self):
        return self.username



class YourModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view the instance"),
            ("can_create", "Can create instances"),
            ("can_edit", "Can edit instances"),
            ("can_delete", "Can delete instances"),
        ]

