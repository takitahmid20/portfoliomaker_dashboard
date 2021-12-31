from django.shortcuts import render
from mycv.models import blogModel

from django.contrib.sites.shortcuts import get_current_site


def homePage(request):
    blogdata = blogModel.objects.all().order_by('-blog_created')
    context = {'blogdata':blogdata}
    return render(request, 'cvhomepage/index.html', context)


def blogPage(request):
    blogdata = blogModel.objects.all().order_by('-blog_created')
    context = {'blogdata':blogdata}
    return render(request, 'cvhomepage/blog.html', context)


def singleBlogPage(request, pk):
    blog = blogModel.objects.get(id=pk)
    current_site = get_current_site(request)
    context = {'blog':blog, 'domain':current_site}
    return render(request, 'cvhomepage/single_blog.html', context)


def notFoundPage(request, exception):
    return render(request, '404.html')
