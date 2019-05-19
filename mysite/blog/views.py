from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Category
from .models import Comment
from django.utils import timezone
from .form import PostForm, CommentForm, CategoryForm
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf.global_settings import TEMPLATES
import math

#TEMPLATES[0]['OPTIONS']['context_processors'].insert(0, 'django.core.context_processors.request')

# Create your views here.
 
def category_setting(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect(category_setting)
    else:    
        form = CategoryForm()
    return render(request, 'blog/main_page.html', {'form': form})


def post_list(request, num=1):
    list = Post.objects.filter(number = num).order_by('-created_date') # 카테고리 별로 불러오기
    page = request.GET.get('page',1)
    cur_max = int((int(page)-1) / 5) * 5 + 5;
    cur_min = int((int(page)-1) / 5) * 5 + 1;
    paginator = Paginator(list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    max_len = math.ceil(len(list)/5.0)
    return render(request, 'blog/post_list.html', {'posts' : posts, 'num':num, 'max_len': max_len, 'cur_max':cur_max,'cur_min':cur_min,})


def post_detail(request, number, pk): #  포스트 출력 및 댓글입력
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(num = pk).order_by('created_date')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_date = timezone.now()
            comment.num = pk
            comment.save()
            return redirect(post_detail, number=number, pk=pk)
    else:    
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'num' : number, "comments":comment, 'form':form, })


def post_new(request, number):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) # 뒤에 request.FILES 안적으면 파일 안올라감
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.created_date = timezone.now()
            post.number = number
            post.save()
            return redirect(post_detail, number=number, pk=post.pk)
    else:    
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def comment_new(request, number, pk): # 댓글 달기
    if request.method == "POST":
        form = CommentForm(request.POST) # 뒤에 request.FILES 안적으면 파일 안올라감
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_date = timezone.now()
            comment.num = pk
            comment.save()
            return redirect(post_detail, number=number, pk=pk)
    else:    
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form': form})

def post_edit(request, number, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
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

def category_delete(request,pk):
    category = Category.objects.get(pk = pk)
    category.delete()
    return redirect(category_setting)

def comment_delete(request, number, post_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect(post_detail, number=number, pk=post_pk)

def category_list(request):
    categorys = Category.objects.order_by('pk')
    return render(request, 'blog/base.html', {'categorys': categorys})



