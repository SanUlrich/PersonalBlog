from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.homepage, name="homepage"),

    path('blog/', views.ArticleListView.as_view(), name="article-list"),
    path('blog/<slug:slug>/', views.ArticleDetailView.as_view(), name="article-detail"),
    path('post/', views.create_new_article, name="create-new-article"),

    path('register/', views.register_page, name="registering"),

    path('auth/login/', LoginView.as_view(), name="login"),
    path('auth/logout/', LogoutView.as_view(), name="logout"),

    path('auth/password-reset/', PasswordResetView.as_view(), name="password-reset"),
    path('auth/password-reset/done/', PasswordResetDoneView.as_view(), name="password-reset-done"),
    path('auth/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path('auth/reset/done/', PasswordResetCompleteView.as_view(), name="password-reset-complete"),
]
