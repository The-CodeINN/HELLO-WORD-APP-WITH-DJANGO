from django.views.generic import ListView, TemplateView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
  
class AboutPageView(TemplateView):
    template_name = 'about.html'