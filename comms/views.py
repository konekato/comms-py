from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-id')
    return render(request, 'home.html', context={
        'articles': articles,
    })

def user_articles(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles = Article.objects.filter(user_id=user.id).order_by('-id')
    return render(request, 'user_articles.html', context={
        'u': user,
        'articles': articles,
    })

def user_article(request, username, article_id):
    user = get_object_or_404(get_user_model(), username=username)
    article = get_object_or_404(Article, pk=article_id, user_id = user.id)
    return render(request, 'user_article.html', context={
        'u': user,
        'article': article,
    })

@login_required
def create(request):
    return render(request, 'create.html')