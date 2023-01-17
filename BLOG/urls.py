from . import views
from django.urls import path
from .views import AllPostView
from django.views.generic import TemplateView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
    )
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
from django.urls import include

# A list of url patterns.
urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
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
