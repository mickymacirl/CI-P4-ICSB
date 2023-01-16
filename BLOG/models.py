from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# A tuple of tuples.
STATUS = (
    (0, "Draft"),
    (1, "Published"),
    (2, "Disabled"),
)


# The Post model has a title, slug, author, updated_on, category, content, created_on, status and
# is_pinned field. 
# 
# The title field is a CharField. It has a max_length attribute set to 100. It is unique and has a
# validator that only allows alphabet, spaces and - characters
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
    #    ordering = ['-created_on']

    def save(self, *args, **kwargs):
        """
        If the slug field is empty, then add spaces to the title with dashes and save to the slug field.
        """
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    


# Comment model that has a post, author, name, email, body, created_on, active, and status
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
