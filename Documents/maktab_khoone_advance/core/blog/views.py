from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def indexView(request):

    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'sina'
        context['post'] = Post.objects.all()
        return context

''' FBV for redirect
from django.shortcuts import redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhoone.com')
'''
 
class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class PostList(PermissionRequiredMixin , LoginRequiredMixin, ListView):
    # queryset = Post.objects.all()
    permission_required = 'blog.view_post'
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'
    # def get_queryset(self):
    #     posts = Post.objects.all()
    #     return posts
    
class PostDetailView(DetailView):
    model = Post

# class PostCreateView(FormView):
#     template_name = 'blog/contact.html'
#     form_class = PostForm
#     success_url = '/blog/post/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"

@api_view()
def api_post_list_view(request):
    return Response({"message":"saloom"})