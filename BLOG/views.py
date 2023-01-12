from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

class PostList(ListView):
    template_name = 'index.html'

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
