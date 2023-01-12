from . import views
from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# This is a list of URL patterns for the blog app.
#urlpatterns = [
#    path('', views.PostList.as_view(), name='home'),
#    # path('<slug:slug>/', views.post_detail, name='post_detail'),
#]