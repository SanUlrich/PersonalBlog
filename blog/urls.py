from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('blog/', views.ArticleListView.as_view(), name="article-list"),
    path('blog/<slug:slug>/', views.ArticleDetailView.as_view(), name="article-detail"),
]
