from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic

from .models import Article
from .forms import RegisterUserForm


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
            return redirect("blog:logging")
    context = {"form": form}
    return render(request, "accounts/register.html", context)
