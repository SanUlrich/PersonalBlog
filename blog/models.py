from django.db import models


class Article(models.Model):
    """
    Article model. Include title, intro, main text and publication/update date.
    """
    article_title = models.CharField("Article title", max_length=255, db_index=True)
    intro = models.TextField("Article intro", blank=True)
    text = models.TextField("Article text")
    publication_date = models.DateField("Publication date", auto_now_add=True)
    update_date = models.DateField("Update date", auto_now=True)
    slug = models.SlugField("URL", max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.article_title

    class Meta:
        ordering = ['-update_date', '-publication_date']
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    comment_text = models.TextField(help_text="Comment")
    username = models.CharField(max_length=255, help_text="Username")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'A comment belonging to "{self.article.article_title}" article'

    class Meta:
        ordering = ['-comment_date']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
