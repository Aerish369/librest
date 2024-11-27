from django.conf import settings
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    published_date = models.DateField()
    tag = models.ManyToManyField('Tag')

    @property
    def availability_status(self):
        active_borrow = self.borrow_set.filter(status='borrowed').exists()
        return not active_borrow

    def __str__(self) -> str:
        return self.title

class Profile(models.Model):
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def username(self):
        return self.user.username

    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name
    
    @property
    def email(self):
        return self.user.email


    def __str__(self) -> str:
        return self.user.first_name + ' ' + self.user.last_name


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True,  blank=True)
    status = models.CharField(max_length=10, choices=[
                                    ('borrowed', 'Borrowed'), 
                                    ('returned', 'Returned')
                                ], 
                                default='borrowed')

    def __str__(self) -> str:
        return f'{self.user.first_name} borrowed {self.book} on {self.borrowed_date} (status:{self.status})'


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.full_name

class Tag(models.Model):
    tag = models.CharField(max_length=155)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.tag