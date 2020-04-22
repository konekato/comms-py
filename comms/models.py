from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Article(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

class ReplyArticle(models.Model):
    reply_from = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="repling_article")
    reply_to = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="replied_article")