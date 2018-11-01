from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    ari = models.air.objects.all()
    return render(request, 'index.html', {'ari': ari})


def blog_page(request, aid):
    ari = models.air.objects.get(pk=aid)
    return render(request, 'blog_page.html', {'ari': ari})


def edit_page(request, aid):
    if aid == 0:
        return render(request, 'edit_page.html')
    else:
        ari = models.air.objects.get(pk=aid)
        return render(request, 'edit_page.html', {'ari': ari})


def edit_action(request):
    aid = request.POST.get('aid', '0')
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')

    if aid == '0':
        models.air.objects.create(title=title, content=content)
        ari = models.air.objects.all()
        return render(request, 'index.html', {'ari': ari})
    else:
        ari = models.air.objects.get(pk=aid)
        ari.title = title
        ari.content = content
        ari.save()
        return render(request, 'blog_page.html', {'ari': ari})


def test(request):
    a = "HHHHHH"
    return render(request, 'blog_page.html', a)
