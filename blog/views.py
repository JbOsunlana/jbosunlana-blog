from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
# Create your views here.
from django.urls import reverse_lazy
from .models import Post, Comment



class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all
        return context

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class AddCommentView(LoginRequiredMixin, CreateView):

    model = Comment
    template_name = 'add_comment.html'
    fields = ('__all__')