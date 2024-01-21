from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    TemplateView, ListView, DetailView, FormView, DeleteView, UpdateView
)
from apps.blog.models import Category, Post
from django.contrib.auth.models import User

# Create your views here.





class IndexPage(TemplateView):
    template_name = "index.html"
    
    
class ProductsView(TemplateView):
    template_name = "products.html"


class CategoryListView(TemplateView):
    template_name = "category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


    
class PostListView(TemplateView):
    template_name = "post_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(is_draft=False) 
        latest_four_posts = Post.objects.filter(is_draft=False).order_by('-created') 
        if len(latest_four_posts) < 4:
            context["latest_four_posts"] = latest_four_posts
        else:
            context["latest_four_posts"] = latest_four_posts[:4]

        context["categories"] = Category.objects.all()

        return context

    def get_queryset(self):
        qs = Post.objects.filter(is_draft=False)
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            qs = Post.objects.filter(is_draft=False, category__slug=category_slug)
            return qs
        return Post.objects.filter(is_draft=False)
    

class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by('-created') 
        if len(latest_posts) < 4:
            context["latest_posts"] = latest__posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()

        return context



from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostCreateForm


class PostCreateView(LoginRequiredMixin, FormView):
    model = Post
    form_class = PostCreateForm 
    success_url = reverse_lazy("index")
    login_url = reverse_lazy("login")
    template_name = "post_create.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user 
        post.save()
        return super().form_valid(form) 

    
class AuthorPostsListView(LoginRequiredMixin, ListView):
    template_name = "author_posts.html"
    model = Post


    def get_queryset(self):
        qs = Post.objects.filter(author=self.request.user)  
        return qs

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(is_draft=False).order_by("-created")
        if len(latest_posts) < 4:
            context["latest_posts"] = latest_posts
        else:
            context["latest_posts"] = latest_posts[:4]

        context["categories"] = Category.objects.all()

        return context



from django.http import Http404



def delete_author_post(request, pk):
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")

    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect(reverse_lazy("author_posts"))


def deactivate_author_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.is_draft = True
    post.save(update_fields=["is_draft"])
    return redirect(reverse_lazy("author_posts"))


def activate_author_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.is_draft = False
    post.save(update_fields=["is_draft"])
    return redirect(reverse_lazy("author_posts"))


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostCreateForm
    model = Post 
    success_url= reverse_lazy("author_posts")
    template_name = "post_create.html"










