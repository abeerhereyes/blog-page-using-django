from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Post
from django.views.generic import ListView ,DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

# Create your views here.\

def home(request):
    context = {
        'posts'  : Post.objects.all(),

    }
    return render( request , 'blog/main.html' , context=context )


class PostListView( LoginRequiredMixin , ListView):
    model = Post
    template_name = 'blog/main.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin , DetailView):
    model = Post
    
class PostCreatelView(LoginRequiredMixin , CreateView):
    model = Post

    
    fields = ['title', 'content']
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user  # Set the author of the post to the current user.
        return super().form_valid(form)



class PostUpdatelView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user  # Set the author of the post to the current user.
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        
        return False
    

class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/home'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        
        return False

def about(request):
    return render(request , 'blog/about.html')