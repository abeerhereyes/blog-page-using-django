from django.urls import path
from . import views
from .views import PostListView , PostDetailView , PostCreatelView , PostUpdatelView , PostDeleteView

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path("about/" , views.about , name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/new/', PostCreatelView.as_view() , name='post-create'),
    path('post/<int:pk>/update/', PostUpdatelView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),

    
]