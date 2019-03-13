from django.contrib import admin
from .models import Author, Article, Rating

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Rating)
