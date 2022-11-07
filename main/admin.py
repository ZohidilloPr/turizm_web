from django.contrib import admin
from custom_user.forms import NewPost
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
    BackgroundImageForNews,
    BackgroundImageForAreas,
)

# Register your models here
class PostAdmin(admin.ModelAdmin):
    form = NewPost
admin.site.register(Post, PostAdmin)
admin.site.register(News)
admin.site.register(Hududlar)
admin.site.register(PhotoArxiv)
admin.site.register(VideoArxiv)
admin.site.register(NavbarName)
admin.site.register(WebSiteName)
admin.site.register(NavbarItems)
admin.site.register(HeaderSlider)
admin.site.register(BackgroundImage)
admin.site.register(BackgroundImageForNews)
admin.site.register(BackgroundImageForAreas)
