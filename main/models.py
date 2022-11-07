from PIL import Image
from django.db import models
from custom_user.models import CustomUser
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# max_length
# verbose_name

# globals varible
l = 200
m = models
M = m.Model

statusUz = (
    ('tuman', 'tuman'),
    ('shaxar', 'shaxar')
)
statusRu = (
    ('город', 'город'),
    ('район', 'район')
)
statusEn = (
    ('city', 'city'),
    ('district', 'district')
)


class AutoDate(M):
    uz_name = m.CharField(max_length=l)
    ru_name = m.CharField(max_length=l, null=True, blank=True)
    en_name = m.CharField(max_length=l, null=True, blank=True)
    add_time = m.DateTimeField(auto_now_add=True)
    post_view = m.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.uz_name

class NavbarName(M):
    """ Navbar nomi """
    uz_name = m.CharField(max_length=l)
    ru_name = m.CharField(max_length=l, null=True, blank=True)
    en_name = m.CharField(max_length=l, null=True, blank=True)
    navbar_img = ResizedImageField(size=[1920, 1080], upload_to="navbarname/", null=True, blank=True)
    slug = m.SlugField(max_length=l, unique=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uz_name

class NavbarItems(AutoDate):
    """ Navbarni bo'limlari uchun items """
    navbar = m.ForeignKey(NavbarName, on_delete=m.CASCADE)
    navbar_img = ResizedImageField(size=[1920, 1080], upload_to='navbaritems/', null=True, blank=True)
    slug = m.SlugField(max_length=l, unique=True)

    def __str__(self):
        return super().__str__()

class Post(M):
    """ Postlar """
    author = m.ForeignKey(CustomUser, on_delete=m.SET_NULL, null=True, blank=True)
    # navbar = m.ForeignKey(NavbarName, on_delete=m.SET_NULL, null=True, blank=True)
    navbaritem = m.ForeignKey(NavbarItems, on_delete=m.SET_NULL, null=True, blank=True)
    post_img = ResizedImageField(size=[1920, 1080],upload_to='posts/')
    uz_title = m.CharField(max_length=l)
    ru_title = m.CharField(max_length=l, null=True, blank=True)
    en_title = m.CharField(max_length=l, null=True, blank=True)
    uz_description = m.CharField(max_length=100)
    ru_description= m.CharField(max_length=l, null=True, blank=True)
    en_description= m.CharField(max_length=l, null=True, blank=True)
    uz_post = RichTextUploadingField()
    ru_post = RichTextUploadingField(null=True, blank=True)
    en_post = RichTextUploadingField(null=True, blank=True)
    slug = m.SlugField(max_length=l, unique=True)
    post_view = m.IntegerField(default=0, null=True, blank=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uz_title

class Hududlar(Post):
    """ Hududlar uchun post """
    navbar = m.ForeignKey(NavbarName,on_delete=m.SET_NULL, null=True, blank=True)

    def __str__(self):
        return super().__str__()

class News(Post):
    """ Yangiliklar uchun """
    navbar = m.ForeignKey(NavbarName,on_delete=m.SET_NULL, null=True, blank=True)

    def __str__(self):
        return super().__str__()
 
class WebSiteName(AutoDate):
    logo = ResizedImageField(size=[1920, 1080],upload_to='logo/', default='default/logo.png')
    """ NavBardagi web site nomi """
    def __str__(self):
        return super().__str__()

class PhotoArxiv(M):
    photos = ResizedImageField(size=[1920, 1080], upload_to='photoArxiv/')
    add_time = m.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.photos}"
    

class VideoArxiv(M):
    foster = ResizedImageField(size=[1920, 1080],upload_to='video_fosters/')
    video = m.FileField(upload_to='videos/')
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.foster}"

class BackgroundImage(M):
    bg_img = ResizedImageField(size=[1920, 1080],upload_to='backgroundImage/')

    def __str__(self):
        return str(self.bg_img)

class BackgroundImageForAreas(M):
    """ Hududlar uchun rasmlar """
    bg_img = ResizedImageField(size=[1920, 1080],upload_to="BackgroundImageForAreas/")    

    def __str__(self):
        return f"{self.bg_img}"

class BackgroundImageForNews(M):
    """ Yangiliklar uchun rasmlar """
    bg_img = ResizedImageField(size=[1920, 1080],upload_to="BackgroundImageForNews/")    
    
    def __str__(self):
        return f"{self.bg_img}"

class HeaderSlider(Post):
    """ Headerdagi carousel uchun """

    def __str__(self):
        return super().__str__()
