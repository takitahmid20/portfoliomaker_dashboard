from django.shortcuts import render
from mycv.models import blogModel


def homePage(request):
    blogdata = blogModel.objects.all()
    context = {'blogdata':blogdata}
    return render(request, 'cvhomepage/index.html', context)


def blogPage(request):
    blogdata = blogModel.objects.all()
    context = {'blogdata':blogdata}
    return render(request, 'cvhomepage/blog.html', context)


def singleBlogPage(request):
    context ={}
    return render(request, 'cvhomepage/single_blog.html', context)


def notFoundPage(request, exception):
    return render(request, '404.html')
