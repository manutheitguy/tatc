import requests

from django.shortcuts import render

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return render(request, 'home/index.html')

def about(request):

    return render(request, 'home/about.html')

def services(request):

    return render(request, 'home/services.html')

def blog(request):

    return render(request, 'home/blog.html', {
    'title': 'Latest Posts'
})