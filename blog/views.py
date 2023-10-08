from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Posts
from .forms import PostForm

# Create your views here.


def blog(request):
    posts = Posts.objects.all()
    context = {
        'title': 'My blog',
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context=context)


def blog_detail(request, post_id):
    post = Posts.objects.get(id=post_id)
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, 'blog/blog_detail.html', context=context)


@login_required(login_url='/portfolio/')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    forms = PostForm()
    context = {
        'title': 'Create post',
        'form': forms
    }
    return render(request, 'blog/create.html', context=context)