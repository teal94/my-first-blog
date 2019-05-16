from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Category
from django.utils import timezone
from .form import PostForm
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
 
def post_list(request, num=1):
    posts = Post.objects.filter(number = num).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts, 'num':num})

def post_detail(request, number, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'num' : number})

def post_new(request, number):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.created_date = timezone.now()
            post.number = number
            post.save()
            return redirect(post_list, num=number)
    else:    
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, number, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, number = number, pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, number, pk):
    post = Post.objects.get(pk = pk)
    post.delete()
    return redirect(post_list, num=number)

def category_list(request):
    categorys = Category.objects.order_by('number')
    return render(request, 'blog/base.html', {'categorys': categorys})
