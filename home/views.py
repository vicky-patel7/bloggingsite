from email import message
from turtle import title
from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from myblog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

def signUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 12:
            messages.error(request, "Username must be less than 12 characters.")
            return redirect('index')
        if not username.isalnum():
            messages.error(request, "Username must contain letters and numbers")
            return redirect('index')
        if pass1 != pass2:
            messages.error(request, "Passwords didnot match")
            return redirect('index')

        myuser = User.objects.create_user(username = username, email = email, password = pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser = form.save(commit=False)
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('index')
    else:
        return HttpResponse("404 - NOT FOUND")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

def handleLogin(request):
    if request.method == "POST":
        username = request.POST['loginusername']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully loged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('index')
    else:
        return HttpResponse("404 - Not Found")