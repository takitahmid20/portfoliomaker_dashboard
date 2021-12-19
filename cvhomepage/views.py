from django.shortcuts import render


def homePage(request):
    context = {}
    return render(request, 'cvhomepage/index.html', context)


def notFoundPage(request, exception):
    return render(request, '404.html')
