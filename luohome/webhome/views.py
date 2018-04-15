from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def hello(request):
    ari = models.air.objects.get(pk=1)
    return render(request,'index.html',{'ari':ari})
