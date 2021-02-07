from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.
from bet.models import Article, Category


def homePage(request):
    articles = Article.objects.all().order_by('-id')[:4][::-1]
    context ={
        'articles':articles,
    }
    return render(request,'bet/index.html',context)


def articleList(request,slug):
    cat = Category.objects.get(slug=slug)
    articles = Article.objects.filter(cat=cat.id)
    sidePosts = Article.objects.all().order_by('-id')[:5][::-1]
    return render(request,'bet/articleList.html',{'slug':slug, 'articles':articles,'sidePosts':sidePosts,'cat':cat})


def postDetail(request,categorySlug,postSlug):
    sidePosts = Article.objects.all().order_by('-id')[:5][::-1]
    post = Article.objects.get(slug=postSlug)
    context={
        'sidePosts':sidePosts,
        'post': post
    }
    return render(request,'bet/postDetail.html',context)