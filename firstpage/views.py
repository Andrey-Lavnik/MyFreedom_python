from django.http import HttpResponse
from django.shortcuts import render

def index_page(request):
    n = "vlad"
    return render(request, 'firstpage/index.html', context={'name': n})