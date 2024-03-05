from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'isbn']
    list_display = ['title', 'description', 'isbn']

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Book_Author)
admin.site.register(Review)