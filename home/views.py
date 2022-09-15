from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render (request, 'home/index.html')
    # return HttpResponse('This is home page')

def about(request):
    return render (request, 'home/about.html')

def contact(request):
    return render (request, 'home/contact.html')