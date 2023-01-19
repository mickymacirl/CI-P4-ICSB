from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
"""
CRUD
"""
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm


class AllPostView(ListView):
    """
    This class is a list view of all the posts in the database, and it will
    paginate the results by 5 posts per page."
    URL for this view.:
    url(r'^all/$', AllPostView.as_view(), name='all_posts'),
    """
    model = Post
    template_name = 'all_posts.html'
    context_object_name = 'all_posts'
    paginate_by = 5

    def get_queryset(self):
        """
        If the user is a superuser or staff, show all posts. If the user is 
        logged in, show only published posts. If the user is not logged in, 
        show nothing
        :return: The get_queryset method is being overridden to return a 
        queryset of all posts if the user is a superuser or staff, a queryset 
        of all posts with status 1 if the user is authenticated, and an
        empty queryset if the user is not authenticated.
        """
        if self.request.user.is_superuser or self.request.user.is_staff:
            return Post.objects.all()
        elif self.request.user.is_authenticated:
            return Post.objects.filter(status='1')
        else:
            return Post.objects.none()


def about(request):
    """
    About Page
    Takes a request object as an argument, and returns a response object
    :param request: This is the request object that is sent to the view
    :return: The about.html file is being returned.
    """
    return render(request, 'about.html')


def contact(request):
    """
    Contact Page
    Takes a request, and returns a response
    :param request: This is the request object that is sent to the view
    :return: The contact.html file is being returned.
    """
    return render(request, 'contact.html')


class PostList(generic.ListView):
    """
    Home Page View
    This view will return a list of posts that are published and ordered by the
    most recently published post.
    The first line of the class defines the model that will be used to retrieve
    objects for the view.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    for i in queryset:
        print("SLUG: ",  i.slug)


def post_detail(request, slug):
    """
    Rendering the template with the context
    :param request: The current request object
    :param slug: The slug is the URL-friendly version of the title
    :return: The template is being rendered with the context.
    """
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    """
    Comment posted
    """
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            """
            Create Comment object but don't save to database yet
            """
            new_comment = comment_form.save(commit=False)
            """
            Assign the current post to the comment
            """
            new_comment.post = post
            """
            Save the comment to the database
            """
            new_comment.save()
    else:
        comment_form = CommentForm()

    """
    Rendering the template with the context.
    """
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def custom_403(request, exception):
    """
    Takes the request and exception as arguments, and returns a rendered
    template
    :param request: The request object
    :param exception: The exception raised by the view
    :return: A 403 error page.
    """
    return render(request, '403.html')


"""
specify a custom view for a 403 error.
"""
handler403 = 'path.to.custom_403'


def handle_500(request):
    """
    Takes a request object as an argument, and returns a response object that
    renders the 500.html template
    :param request: The request object used to generate this response
    :return: The 500.html page is being returned.
    """
    return render(request, '500.html')


def get_success_url(self):
    """
    Returns the URL of the detail page for the object that was just created
    :return: The reverse_lazy function is being used to return the url of the
    post_detail view.
    """
    return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


class PostListView(ListView, LoginRequiredMixin):
    """
    List view of Post objects, and it's called PostListView.
    The first line of the class tells Django to use the ListView generic view.
    The next line tells# Django to use the post_list.html template.
    The last line tells Django to use the context name posts
    for the list of posts
    """
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView, LoginRequiredMixin):
    model = Post
    template_name = 'post_view.html'


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'post_create_form.html'
    fields = ['author', 'title', 'content', 'category', 'status', 'is_pinned']
    context_object_name = 'post_create'
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = 'post_edit_form.html'
    fields = ['author', 'title', 'content', 'category', 'status', 'is_pinned']
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/posts/'


class CommentApprovalView(UpdateView, LoginRequiredMixin):
    model = Comment
    # add 
    commentsAll = Comment.objects.all()
    commentsActive = Comment.objects.filter(active=True)
    commentsStatus1 = Comment.objects.filter(status='approved')
    commentStatus2s = Comment.objects.exclude(status='rejected')
    
    template_name = 'comment_approval_form.html'
    fields = ['status', 'active']
    context_object_name = 'comment/'
    success_url = reverse_lazy('home')
