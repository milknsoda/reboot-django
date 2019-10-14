from django.shortcuts import render, redirect
from .models import Article, Comment
from .form import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def new(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('/start/')
    else:
        article_form = ArticleForm()
        context = {
            'article_form': article_form
        }
        return render(request, 'form.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'detail.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article = article_form.save()
            return redirect(f'/start/detail/{article_pk}')
    else:
        article_form = ArticleForm(instance=article)
        context = {
            'article_form': article_form
        }
        return render(request, 'update.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('/start/')
    else:
        return redirect(f'/start/detail/{article_pk}')

def commentcreate(request, article_pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect(f'/start/detail/{article_pk}')

def commentdelete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect(f'/start/detail/{article_pk}')

