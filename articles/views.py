from django.shortcuts import render, redirect
from .models import Article
from IPython import embed

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.image = request.FILES.get('image')
    # articles.created_at = request.GET.get('created_at')
    # articles.updated_at = request.GET.get('updated_at')
    article.save()
    # embed()

    return redirect('/articles/')

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()

    return redirect('/articles/')

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # if article.title != request.GET.get('title') or article.content != request.GET.get('content'): 없어도 가능합니다?
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    
    return redirect(f'/articles/{article_pk}')