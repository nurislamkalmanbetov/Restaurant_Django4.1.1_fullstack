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
        return context
    
    














