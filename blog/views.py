from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    print(blogs)
    context={
        'blog_list':blogs

    }
    return render(request,'blogs/blog_section.html',context)
