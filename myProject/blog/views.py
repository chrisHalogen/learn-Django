from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def archive(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request,'blog/archive.html', context)

def detail(request,pk):
    blog = BlogPost.objects.get(pk=pk)
    context = {
        'blog' : blog
    }
    return render(request,'blog/detail.html', context)