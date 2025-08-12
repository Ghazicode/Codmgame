from django.shortcuts import render, get_object_or_404
from .models import Article 
from django.core.paginator import Paginator



# def article(request):
#     articles = Article.objects.filter(status = True)
    
#     return render(request, 'blog/blog.html', {'articles':articles})





def article(request):
    articles = Article.objects.filter(status = True)
    return render(request, 'blog/blog.html', {'articles':articles})

def article_detail(request, search):
    article = Article.objects.get(search = search)
    return render(request, "blog/article-detail.html", {'article':article})

