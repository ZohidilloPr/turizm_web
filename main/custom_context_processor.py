import random
from .models import (
    Post,
    News,
    Hududlar,
    NavbarName,
    PhotoArxiv,
    VideoArxiv,
    WebSiteName,
    NavbarItems,
    HeaderSlider,
    BackgroundImage,
    BackgroundImageForAreas,
    BackgroundImageForNews,
)

def common_variables(request):
    arealist = Hududlar.objects.all()
    web_name = WebSiteName.objects.last()
    BgFon = BackgroundImage.objects.last()
    navbaritems = NavbarItems.objects.all()
    navbarName0 = NavbarName.objects.all()[0]
    navbarName1 = NavbarName.objects.all()[1]
    navbarName2 = NavbarName.objects.all()[2]
    bgNews = BackgroundImageForNews.objects.last()
    bgAreas = BackgroundImageForAreas.objects.last()
    news = News.objects.all().order_by('-add_time')[:8]
    news_left = News.objects.all().order_by('-add_time')[:4]
    photos = PhotoArxiv.objects.all().order_by('-add_time')[:7]
    videos = VideoArxiv.objects.all().order_by('-add_time')[:3]
    slideshow = PhotoArxiv.objects.all().order_by('-add_time')[:100]
    header_slider = HeaderSlider.objects.all().order_by('-add_time')[:5]
    shrines = Post.objects.filter(navbaritem__slug='ziyoratgohlar')[:8]
    randomBG = random.choice(PhotoArxiv.objects.all())

    context = {
        'news':news,
        'bgfon': BgFon,
        'bgNews':bgNews,
        'photos':photos,
        'videos':videos, 
        'bgAreas':bgAreas,
        'shrines':shrines,
        'nav0':navbarName0, 
        'nav1':navbarName1, 
        'nav2':navbarName2,
        'arealist':arealist,
        'web_name': web_name,
        'randomBG': randomBG,
        'news_left':news_left,
        'slideshow':slideshow,
        'navbaritems':navbaritems,
        'header_slider':header_slider,
    }
    return context