from turtle import title
from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from myblog.models import Post
# Create your views here.
def index(request):
    return render (request, 'home/index.html')
    # return HttpResponse('This is home page')

def about(request):
    return render (request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        context = Contact(name = name, email = email, phone = phone, content = content)
        if len(name)<2 or len(email) <3 or len(phone) < 10 or len(content) < 10:
            messages.error(request, "Please fill the form correctly.")
        else:
            context = Contact(name = name, email = email, phone = phone, content = content)
            context.save()
            messages.success(request, "You message has been successfully sent.")

    return render (request, 'home/contact.html')

def search(request):
    query=request.GET['search']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)