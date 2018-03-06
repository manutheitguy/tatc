import requests

from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def trading(request):
    return render(request, 'home/trading.html')

def logistics(request):
    return render(request, 'home/logistics_list.html')

def imports(request):
    return render(request, 'home/imports_list.html')

def exports(request):
    return render(request, 'home/exports_list.html')

def solutions(request):
    return render(request, 'home/solutions_list.html')
