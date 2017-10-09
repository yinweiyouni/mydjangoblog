from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from .forms import CommentForm
# Create your views here.


def post_comment(request, comment_pk):
    post = get_object_or_404(Blog, pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
    else:
        comments = post.comments_set().all()
        context = {
            'post': post,
            'form': CommentForm(),
            'comments': comments,
        }
        return render(request, 'blog/detail.html', context=context)


