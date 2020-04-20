from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-id')
    return render(request, 'home.html', context={
        'articles': articles,
    })

@login_required
def create(request):
    return render(request, 'create.html')