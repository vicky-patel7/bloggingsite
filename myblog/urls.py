from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('postComment', views.postComment, name = 'postComent'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]
