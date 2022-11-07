from django.urls import path
from .views import (
    Logout, root, PostFilterList, PostList, DeletePost, AddPost, UpdatePost, AddAreas,
    UpdateAreas, AreasList, NewsList, AddNews, UpdateNews, BGAreas, BGNews, 
    SliderList, AddSlider, UpdateSlider, AddNavbar,  AddWebName, BGMain, AddPhoto, MultiplePhotos
)
app_name = 'users'

urlpatterns = [
    path('user/logout/', Logout, name='logout'),

    # post list
    path('root/', root, name='root'),
    path('root/list/', PostList.as_view(), name='postlist'),
    path('root/post/new/', AddPost.as_view(), name='newpost'),
    path('root/list/<slug>/', PostFilterList, name='postfilterlist'),
    path('root/post/delete/<slug>/', DeletePost.as_view(), name='deletepost'),
    path('root/post/update/<slug>/', UpdatePost.as_view(), name='updatepost'),
    
    # areas list
    path('root/list/all/areas/', AreasList.as_view(), name='areaslist'),
    path('root/areas/new/', AddAreas.as_view(), name='addarea'),
    path('root/areas/update/<pk>/', UpdateAreas.as_view(), name='updateareas'),
    
    # news list
    path('root/list/all/news/', NewsList.as_view(), name='newslist'),
    path('root/news/new/', AddNews.as_view(), name='addnews'),
    path('root/news/update/<pk>/', UpdateNews.as_view(), name='updatenews'),

    # header slider list
    path('root/list/all/slider/', SliderList.as_view(), name='sliderlist'),
    path('root/slider/', AddSlider.as_view(), name='addslider'),
    path('root/slider/update/<pk>/', UpdateSlider.as_view(), name='updateslider'),

    # bg main
    path('root/bg/main/new/', BGMain.as_view(), name='bgmain'),

    # bg areas
    path('root/bgareas/new/', BGAreas.as_view(), name='bgareas'),

    # bg news
    path('root/bgnews/new/', BGNews.as_view(), name='bgnews'),

    # new navbar
    path('root/navbar/new/', AddNavbar.as_view(), name='addnavbar'),

    # new rasm
    path('root/photo/new/', AddPhoto.as_view(), name='addphoto'),

    # new rasmlar
    path('root/photos/new/', MultiplePhotos, name='addphotos'),

    # new web name
    path('root/web/name/new/', AddWebName.as_view(), name='addwebname'),

]