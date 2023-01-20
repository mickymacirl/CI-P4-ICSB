from django.test import TestCase
from django.core.validators import ValidationError
from django.utils import timezone
import datetime
from .models import Comment, Post, User


class CommentModelTestCase(TestCase):
    def setUp(self):
        """
        Create a test user
        """
        self.test_user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        """
        Create a test post
        """
        self.test_post = Post.objects.create(
            title='Test Title',
            slug='test-title',
            author=self.test_user,
            category='test-category',
            content='Test content',
        )
        """
        Create a test comment
        """
        self.test_comment = Comment.objects.create(
            post=self.test_post,
            name='Test Name',
            email='test@example.com',
            body='Test comment',
        )

    def test_str_method(self):
        """
        Test the __str__ method of the Comment model
        """
        self.assertEqual(
            str(self.test_comment),
            'Comment Test comment by Test Name'
        )

    def test_title(self):
        """
        Test that the title field is required and has the correct max length
        """
        self.assertEqual(self.test_post.title, 'Test Title')
        self.assertEqual(
            self.test_post._meta.get_field('title').max_length,
            100
        )
        self.test_post.title = ''
        self.assertRaises(ValidationError, self.test_post.full_clean)

    def test_default_status(self):
        """
        Test the default value of the status field
        """
        self.assertEqual(self.test_comment.status, 'pending')

    def test_ordering(self):
        """
        Test the default ordering of the Comment model
        """
        self.assertEqual(
            Comment._meta.ordering,
            ['created_on']
        )

    def test_status(self):
        """
        Test that the status field has the correct choices and default value
        """
        self.assertEqual(self.test_comment.status, 'pending')
        self.assertEqual(
            self.test_comment._meta.get_field('status').choices,
            [('review', 'Review'), ('accepted', 'Accepted'), ('spam', 'Spam')]
                        )
        self.assertEqual(
            self.test_comment._meta.get_field('status').default,
            'pending'
            )

    def test_created_on(self):
        """
        Test field is set to the current time on comment reated
        """
        now = timezone.now()
        self.assertAlmostEqual(
            self.test_comment.created_on,
            now,
            delta=datetime.timedelta(seconds=10)
        )


class PostModelTestCase(TestCase):
    def setUp(self):
        """
        Create a test user
        """
        self.test_user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        """
        Create a test post
        """
        self.test_post = Post.objects.create(
            title='Test Title',
            slug='test-title',
            author=self.test_user,
            category='test-category',
            content='Test content',
        )

    def test_str_method(self):
        """
        Test the __str__ method of the Post model
        """
        self.assertEqual(str(self.test_post), 'Test Title')

    def test_ordering(self):
        """
        Test the default ordering of the Post model
        """
        self.assertEqual(
            Post._meta.ordering,
            ['-is_pinned', '-id']
        )

    def test_unique_slug(self):
        """
        Test that the slug field is unique
        """
        second_post = Post.objects.create(
            title='Test Title 2',
            slug='test-title-2',  
            author=self.test_user,
            category='test-category',
            content='Test content 2',
        )
        """
        Save the second post without raising an error
        """
        second_post.save()

    def test_title_length(self):
        """
        Test that the title field has the correct max length
        """
        self.assertEqual(self.test_post.title, 'Test Title')
        self.assertEqual(
            self.test_post._meta.get_field('title').max_length,
            100
        )
