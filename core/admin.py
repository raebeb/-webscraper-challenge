from django.contrib import admin
from core.models import Book

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)

# Register your models here.
