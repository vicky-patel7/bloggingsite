# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse, redirect
from myblog.models import Post, BlogComment
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'myblog/blogHome.html', context)
    # return HttpResponse('This is home for blog post')


def blogPost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    comments = BlogComment.objects.filter(post = post)
    context = {'post':post, 'comments':comments, 'user' : request.user}
    # print(post)
    return render(request, 'myblog/blogPost.html', context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno = postSno)

        comment = BlogComment(comment=comment, user = user, post = post)
        comment.save()
        messages.success(request, "You comment has been successfully posted")
    return redirect(f"/blog/{post.slug}")
