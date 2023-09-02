from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("process_images", views.process_images, name="process_images"),
]