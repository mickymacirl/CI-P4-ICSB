from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from pure_pagination import PaginationMixin
from django.views.generic.list import ListView
from .models import Post, Comment
from .forms import CommentForm

# "This is a list view of the Post model,
# and it will be rendered using the template
# index.html."
# The template_name attribute is used to tell
# Django which template to use for a view.
# In this case, we're using the template index.html


# class PostList(ListView):
#    template_name = 'index.html'

# class AllPostView(PaginationMixin, ListView):
#     model = Post
#     template_name = 'all_posts.html'
#     context_object_name = 'all_posts'
#     paginate_by = 5  # Number of items per page


class AllPostView(ListView):
    model = Post
    template_name = 'all_posts.html'
    context_object_name = 'all_posts'
    paginate_by = 5


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


# This view will return a list of posts that are published and ordered by the
# most recently published post.
# The first line of the class defines the model that will be used to retrieve
# objects for the view.
class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')[:6]
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5


# def post_list(request):
    """
    It takes a request, gets the first five posts from the database, and
    returns a rendered template with the list of posts
    :param request: The request is what's sent from the browser to the server.
    It contains all the     information about the request, such as the HTTP
    method, the GET and POST parameters, the cookies, etc
    :return: The post_list is being returned.
    """
#    post_list = Post.objects.all()[:5]
#    return render(request, 'index.html', {'post_list': post_list})


def post_detail(request, slug):
    """
    It's rendering the template with the context
    :param request: The current request object
    :param slug: The slug is the URL-friendly version of the title
    :return: The template is being rendered with the context.
    """
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

# It's rendering the template with the context.
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def custom_403(request, exception):
    return render(request, '403.html')

# in urls.py
handler403 = 'path.to.custom_403'

def handle_500(request):
    return render(request, '500.html')
