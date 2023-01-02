from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class SarablogListView(ListView):
    model = Post
    template_name = "home.html"
    
class SarablogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    

    
