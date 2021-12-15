from django.shortcuts import render


def homePage(request):
    context = {}
    return render(request, 'cvhomepage/index.html', context)
