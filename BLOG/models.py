from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# A tuple of tuples.
STATUS = (
    (0, "Draft"),
    (1, "Published"),
    (2, "Disabled"),
)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, validators=[RegexValidator(r'^[a-zA-Z\s-]+$', 'Only alphabet, spaces and - characters are allowed')])
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
        # ordering = ['-created_on']

    def __str__(self):
        return self.title

# class Post(models.Model):
#    title = models.CharField(max_length=200, unique=True)
#    slug = models.SlugField(max_length=200, unique=True)
#    author = models.ForeignKey(
#        User, on_delete=models.CASCADE, related_name='blog_posts')
#    updated_on = models.DateTimeField(auto_now=True)
#    category = models.CharField(max_length=200, unique=False)
#    content = models.TextField()
#    created_on = models.DateTimeField(auto_now_add=True)
#    status = models.IntegerField(choices=STATUS, default=2)
#    is_pinned = models.BooleanField(default=False)

#    class Meta:
#        ordering = ['-is_pinned', '-id']
        # ordering = ['-created_on']

#    def __str__(self):
#        return self.title


class Comment(models.Model):
    PENDING = 0
    APPROVED = 1
    REJECTED = 2

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(User, on_delete=models.CASCADE,
    # related_name='comments', null=True)
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
    status = models.CharField(max_length=10, default='pending', choices=[
            ('review', 'Review'), ('accepted', 'Accepted'), ('spam', 'Spam')
        ])

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
