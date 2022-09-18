# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from myblog.models import Post
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'myblog/blogHome.html', context)
    # return HttpResponse('This is home for blog post')


def blogPost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    context = {'post':post}
    # print(post)
    return render(request, 'myblog/blogPost.html', context)