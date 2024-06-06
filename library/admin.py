from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "author_name", "author_surname","publisher")
  
admin.site.register(Book, BookAdmin)