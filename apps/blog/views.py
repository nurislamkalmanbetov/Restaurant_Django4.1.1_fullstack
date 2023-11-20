from django.shortcuts import render
from django.views.generic import TemplateView, ListView
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
    





















    














