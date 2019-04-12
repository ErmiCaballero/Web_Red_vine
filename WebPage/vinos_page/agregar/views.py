from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'lista_de_agregar'

class HomeDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'