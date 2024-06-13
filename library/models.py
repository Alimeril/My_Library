from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


GENRE_CHOICES = (
    ('Literature','Literature'),
    ('Fiction','Fiction'),
    ('Non-Fiction','Non-Fiction'),
    ('Novel','Novel'),
    ('Poem','Poem'),
    ('Biography','Biography'),
    ('Science','Science'),
    ('Philosophy','Philosophy'),
    ('Art','Art'),
    ('Cinema','Cinema'),
    ('Religion','Religion'),
    ('Other','Other'),
)

class Book(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author_name = models.CharField('Author Name',max_length=50, null = True, blank=True)
    author_surname = models.CharField('Author Surname',max_length=50)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    genre = models.CharField(
        max_length = 20,
        choices = GENRE_CHOICES,
        default = 'Literature'
    )
    created = models.DateTimeField(auto_now_add=True)
    borrowed = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse("library:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title}"