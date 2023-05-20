"""
Module contains classes for implementation models as forms in admin site.
"""

from django.contrib import admin
from .models import Article, Comment


class CommentInLine(admin.TabularInline):
    """
    Inline comment section for particular article.
    """
    model = Comment
    fields = ['username', 'comment_text']
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Displaying the article creation section.
    """
    list_display = ['article_title', 'intro', 'truncate_article_text', 'publication_date']
    prepopulated_fields = {'slug': ('article_title', )}
    inlines = [CommentInLine]

    def truncate_article_text(self, obj):
        """
        Returns truncated article's text for compact view in admin site.
        """
        max_length = 100
        if len(obj.text) > max_length:
            return obj.text[:max_length] + '...'
        return obj.text

    truncate_article_text.short_description = 'text'


admin.site.register(Comment)
