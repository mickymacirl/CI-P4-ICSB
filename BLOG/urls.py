from . import views
from django.urls import path
from .views import AllPostView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
from django.urls import include

# A list of url patterns.
urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('', views.PostList.as_view(), name='home'),
    path('all_posts/', AllPostView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', allauth_views.LoginView.as_view(), name='login'),
]
