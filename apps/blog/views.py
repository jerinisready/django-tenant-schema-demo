from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from apps.blog.models import Blog


class BlogList(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blog-list')

