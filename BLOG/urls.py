from . import views
from django.urls import path
from .views import AllPostView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentApprovalView
    )
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
from django.urls import include

"""
List of URL Patterns
"""
urlpatterns = [
    path('comments/<slug:pk>/', CommentApprovalView.as_view(), name='comment_valid'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/', login_required(PostCreateView.as_view()), name='post_create'),
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_view'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('', views.PostList.as_view(), name='home'),
    path('all_posts/', AllPostView.as_view(), name='all_posts'),
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', allauth_views.LoginView.as_view(), name='login'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
