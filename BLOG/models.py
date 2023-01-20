from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


"""
Tuple of tuples
"""
STATUS = (
    (0, "Draft"),
    (1, "Published"),
    (2, "Disabled"),
)

"""
Post class is a model that has a title, slug, author, updated_on, category,
content, created_on, # status, and is_pinned
"""
msg = 'Only alphabet, spaces and - characters are allowed'


class Post(models.Model):
    title = models.CharField(max_length=100,
                             unique=True,
                             validators=[RegexValidator(
                                r'^[a-zA-Z\s-]+$', msg)]
                             )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts'
                               )
    updated_on = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=200, unique=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=2)
    is_pinned = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=200, unique=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=2)
    is_pinned = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_pinned', '-id']
    #    ordering = ['-created_on']

    def save(self, *args, **kwargs):
        """
        If the slug field is empty, then add
        spaces to the title with dashes and save to the slug field.
        """
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Comment model that has a post, author, name, email, body,
    created_on, active, and status
    """
    PENDING = 0
    APPROVED = 1
    REJECTED = 2

    # A tuple of tuples.
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    """
    CharField that has a max length of 10, a default value of 'pending', 
    and a list of choices.
    """
    status = models.CharField(max_length=10, default='pending', choices=[
            ('review', 'Review'), ('accepted', 'Accepted'), ('spam', 'Spam')
        ])

    class Meta:
        """
        Objects will be returned in the order they were created, with the 
        oldest one first.
        """
        ordering = ['created_on']

    def __str__(self):
        """
        The __str__ function is a special function that is called when you
        all str() on an object
        :return: The body of the comment and the name of the 
        person who posted it.
        """
        return 'Comment {} by {}'.format(self.body, self.name)
