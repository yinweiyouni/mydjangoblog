from django.shortcuts import render,get_object_or_404
from .models import Blog,Category,Tag
import markdown
from comments.forms import CommentForm
# from django.http import HttpResponse
# Create your views here.


def index(request):
    all_post = Blog.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'all_post': all_post
    })


# 文章详情页
def detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    comments = post.comments_set.all()
    form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blog/detail.html', context=context)


# 归档
def archives(request, year, month):
    date_list = Blog.objects.filter(created_time__year=year,  created_time__month=month)\
        .order_by('-created_time')
    return render(request, 'blog/index.html', context={'all_post': date_list})


# 分类
def category(request, pk):
    cates = get_object_or_404(Category, pk=pk)
    posts = Blog.objects.filter(category=cates).order_by('-created_time')
    return render(request, 'Blog/index.html',  context={'all_post': posts})




