from django.shortcuts import render

from django.views.generic import ListView

class PostList(ListView):
    template_name = 'index.html'