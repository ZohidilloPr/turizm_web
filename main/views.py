
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from main.models import (
    Post,
    News, 
    Hududlar, 
    PhotoArxiv,
    NavbarItems, 
    HeaderSlider,
)

# Create your views here.

def Home(request):
    return render(request, 'index.htm')

def Home_ru(request, path):
    return render(request, 'index.htm', context={
        'path':path
    })

def testPk(request):
    return render(request, 'pages/template.htm')

def testAll(request):
    return render(request, 'pages/templateall.htm')

class AreaList(ListView):
    model = Hududlar
    ordering = 'uz_title'
    template_name = 'allpages/areas.htm'

class AreaDetail(DetailView):
    model = Hududlar
    template_name = 'onepages/areasone.htm'

class NewsList(ListView):
    model = News
    paginate_by = 16
    ordering = '-add_time'
    template_name = 'allpages/news.htm'

class NewsDetail(DetailView):
    model = News
    template_name = 'onepages/newsone.htm'

class PhotosList(ListView):
    """ Rasmlar albomi uchun view """
    model = PhotoArxiv
    paginate_by = 50
    ordering = '-add_time'
    template_name = 'allpages/photos.htm'

def PostType(request, slug):
    posts = Post.objects.all().filter(navbaritem__slug=slug)
    navbaritem = NavbarItems.objects.get(slug=slug)
    return render(request, 'allpages/posts.htm', context={
        'object_list':posts,
        'object': navbaritem,
        'slug':slug,
    })

def PostView(request, slug):
    post = Post.objects.get(slug=slug)
    navbar = NavbarItems.objects.get(id=post.navbaritem.id)
    return render(request, 'onepages/post.htm', context={
        'object':post,
        'object_nav': navbar
    })
def SlideView(request, slug):
    post = HeaderSlider.objects.get(slug=slug)
    return render(request, 'onepages/post_slide.htm', context={
        'object':post,
    })