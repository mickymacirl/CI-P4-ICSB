from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

# "This is a list view of the Post model,
# and it will be rendered using the template
# index.html."
# The template_name attribute is used to tell
# Django which template to use for a view.
# In this case, we're using the template index.html


class PostList(ListView):
    template_name = 'index.html'


def about(request):
    """
    It takes a request object as an argument, and returns a response object
    :param request: This is the request object that is sent to the view
    :return: The about.html file is being returned.
    """
    return render(request, 'about.html')


def contact(request):
    """
    It takes a request, and returns a response
    :param request: This is the request object that is sent to the view
    :return: The contact.html file is being returned.
    """
    return render(request, 'contact.html')
