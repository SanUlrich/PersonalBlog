from django.shortcuts import render
from django.views import generic

from .models import Article


def homepage(request):
    """
    Returns simple home page.
    """
    return render(request, "blog/homepage.html")


class ArticleListView(generic.ListView):
    """
    Displays list of all articles with pagination.
    """
    model = Article
    paginate_by = 10
    template_name = "blog/article_list.html"
    context_object_name = "articles"


class ArticleDetailView(generic.DetailView):
    """
    Displays detailed page of particular article.
    """
    model = Article
    template_name = "blog/article_detail.html"
