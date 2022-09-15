# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return render(request, 'myblog/blogHome.html')
    # return HttpResponse('This is home for blog post')


def blogPost(request, slug):
    return render(request, 'myblog/blogPost.html')