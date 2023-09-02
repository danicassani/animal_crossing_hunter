from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .models import Fish, Insect, SeaCreature
import os

def index(request):
    return HttpResponse(render(request, 'searcher/index.html'))

# def process_images(request):
#     for image in os.listdir('images/insects'):
#         name = image.split('.')[0]
#         fish = Fish(name=name, image_path=f'images/fishes/{image}')
#         fish.save()
#     for image in os.listdir('images/insects'):
#         name = image.split('.')[0]
#         insect = Insect(name=name, image_path=f'images/insects/{image}')
#         insect.save()
#     for image in os.listdir('images/sea'):
#         name = image.split('.')[0]
#         sea = SeaCreature(name=name, image_path=f'images/sea/{image}')
#         sea.save()
#     return redirect('index')