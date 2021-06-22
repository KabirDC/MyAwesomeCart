from django.shortcuts import render

# create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')
