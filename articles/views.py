from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    model = Article

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    model = Article
    
