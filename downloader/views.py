# from django.conf import settings
from django.shortcuts import render
from . import functions
from django.http import HttpResponse


def home(request):
    return render(request, 'downloader/home.html', {})

def download(request,url):
    link = functions.downloader(url)
    return render(request, 'downloader/download.html', {"without_watermark": link})

def json(request,url):
    link = functions.downloader(url)
    return HttpResponse(link)

def decide(request):
    url = request.POST.get("url")
    todo = int(request.POST.get("todo"))
    if todo == 1:
        return download(request,url)
    elif todo == 2:
        return json(request,url)
    else:
        return HttpResponse("Are Jigar! Tu Idhar Kidhar?")
