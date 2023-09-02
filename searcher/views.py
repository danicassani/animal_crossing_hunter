from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse(render(request, 'searcher/index.html'))

def process_images(request):
    # TODO: Implement this view
    return redirect('index')