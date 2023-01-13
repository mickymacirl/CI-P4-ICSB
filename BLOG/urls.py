from . import views
from django.urls import path
from .views import AllPostView
from django.views.generic import TemplateView

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('', views.PostList.as_view(), name='home'),
    path('all_posts/', AllPostView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
