from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic

from .models import Article
from .forms import RegisterUserForm, CreateNewArticleForm


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
    paginate_by = 5
    template_name = "blog/article_list.html"
    context_object_name = "articles"


class ArticleDetailView(generic.DetailView):
    """
    Displays detailed page of particular article.
    """
    model = Article
    template_name = "blog/article_detail.html"


def register_page(request):
    """
    Returns the new user registration form.
    """
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f'Welcome {user}!')
            return redirect("blog:login")
    context = {"form": form}
    return render(request, "registration/register.html", context)


def create_new_article(request):
    """
    Displays a form for creating a new article.
    """
    form = CreateNewArticleForm()
    if request.method == "POST":
        form = CreateNewArticleForm(request.POST)
        article = form.save(commit=False)
        article.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'New article added.')
            return redirect("blog:article-detail", slug=article.slug)
    context = {"form": form}
    return render(request, "blog/create_article.html", context)
