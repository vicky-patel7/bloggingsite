from django.contrib import admin
from myblog.models import Post, BlogComment
# Register your models here.
admin.site.register(Post)
admin.site.register(BlogComment)