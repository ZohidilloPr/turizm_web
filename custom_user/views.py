from PIL import Image
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.list import ListView

from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)

from main.models import (
    Post, NavbarItems, Hududlar, News, BackgroundImageForAreas,
    BackgroundImageForNews, HeaderSlider, WebSiteName, BackgroundImage, PhotoArxiv,
)

from .forms import (
    NewPost, NewArea, NewNews, BGAreas, NewHeaderSlider
)

# Create your views here.

def Login(request):
    """ Login uchun """
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Xush kelibsiz! {user.username}')
                return redirect('users:postlist')
            messages.error(request, 'Username yoki passwordda xatolik bo\'lishi mumkun iltimos tekshirib ko\'rib qayta urinib ko\'ring')
        messages.error(request, 'Username yoki passwordda xatolik bo\'lishi mumkun iltimos tekshirib ko\'rib qayta urinib ko\'ring')
    return render(request, 'users/login/login.htm', {'form': form})

def Logout(request):
    logout(request)
    return redirect('home')

# admin panel

def root(request):
    """ admin panel uchun asosiy html fayl """
    return render(request, 'users/adminpanel/root.htm')

def PostFilterList(request, slug):
    """ navbaritem bo'yich filterlaydigan dastur """
    posts = Post.objects.filter(navbaritem__slug=slug)
    nav = NavbarItems.objects.get(slug=slug)
    return render(request, 'users/adminpanel/list/list_filter.htm', context={
        'object_list': posts,
        'section_name':nav,
    })


class PostList(ListView):
    """ Barcha postlar """
    model = Post
    ordering = '-add_time'
    paginate_by = 50
    template_name = 'users/adminpanel/list/list.htm'

class AreasList(ListView):
    """ Hududlar ro'yhati """
    model = Hududlar
    ordering = 'uz_title'
    template_name = 'users/adminpanel/list/list_filter_areas.htm'
# add posts
class AddPost(CreateView, SuccessMessageMixin):
    model = Post
    form_class = NewPost
    template_name = 'users/adminpanel/form/post/new.htm'
    success_url = reverse_lazy('users:newpost')
    success_message = 'Post muaffaqiyatli qo\'shildi!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePost(UpdateView, SuccessMessageMixin):
    model = Post
    form_class = NewPost
    template_name = 'users/adminpanel/form/post/update.htm'
    success_message = 'Post muaffaqiyatli yangilandi!'
    success_url = reverse_lazy('users:postlist')


class DeletePost(DeleteView, SuccessMessageMixin):
    model = Post
    success_message = 'Post muaffaqiyatli o\'chirildi!'
    success_url = reverse_lazy('users:postlist')

# add hududlar 
class AddAreas(CreateView, SuccessMessageMixin):
    model = Hududlar
    form_class = NewArea
    template_name = 'users/adminpanel/form/post/new.htm'
    success_message = 'Post muaffaqiyatli qo\'shildi!!'
    success_url = reverse_lazy('users:areaslist')

class UpdateAreas(UpdateView, SuccessMessageMixin):
    model = Hududlar
    form_class = NewArea
    template_name = 'users/adminpanel/form/post/update.htm'
    success_message = 'Post muaffaqiyatli yangilandi!'
    success_url = reverse_lazy('users:areaslist')

# add news
class NewsList(ListView):
    model = News
    ordering = '-add_time'
    paginate_by = 50
    template_name = 'users/adminpanel/list/list_news.htm'

class AddNews(CreateView, SuccessMessageMixin):
    model = News
    form_class = NewNews
    template_name = 'users/adminpanel/form/post/new.htm'
    success_message = 'Post muaffaqiyatli qo\'shildi!!'
    success_url = reverse_lazy('users:newslist')

class UpdateNews(UpdateView, SuccessMessageMixin):
    model = News
    form_class = NewNews
    template_name = 'users/adminpanel/form/post/update.htm'
    success_message = 'Post muaffaqiyatli yangilandi!'
    success_url = reverse_lazy('users:newslist')

# add Header slider
class SliderList(ListView):
    model = HeaderSlider
    ordering = '-add_time'
    paginate_by = 50
    template_name = 'users/adminpanel/list/list_slider.htm'

class AddSlider(CreateView, SuccessMessageMixin):
    model = HeaderSlider
    form_class = NewHeaderSlider
    template_name = 'users/adminpanel/form/post/new.htm'
    success_message = 'Post muaffaqiyatli qo\'shildi!!'
    success_url = reverse_lazy('users:sliderlist')

class UpdateSlider(UpdateView, SuccessMessageMixin):
    model = HeaderSlider
    form_class = NewHeaderSlider
    template_name = 'users/adminpanel/form/post/update.htm'
    success_message = 'Post muaffaqiyatli yangilandi!'
    success_url = reverse_lazy('users:sliderlist')

class AddNavbar(CreateView, SuccessMessageMixin):
    model = NavbarItems
    fields = ('uz_name','ru_name', 'en_name', 'slug', 'navbar', 'navbar_img')
    template_name = 'users/adminpanel/form/post/default.htm'
    success_url = reverse_lazy('users:postlist')

# rasmlar
class AddPhoto(CreateView, SuccessMessageMixin):
    model = PhotoArxiv
    fields = ('photos',)
    template_name = 'users/adminpanel/form/post/default.htm'
    success_url = reverse_lazy('users:postlist')

class AddWebName(CreateView, SuccessMessageMixin):
    model = WebSiteName
    fields = ('uz_name','ru_name', 'en_name', 'logo')
    template_name = 'users/adminpanel/form/post/default.htm'
    success_url = reverse_lazy('users:postlist')

# background areas photo
class BGAreas(CreateView, SuccessMessageMixin):
    model = BackgroundImageForAreas
    form_class = BGAreas
    template_name = 'users/adminpanel/form/bg/new.htm'
    success_url = reverse_lazy('users:postlist')
    success_message = 'Fon yangilandi'

# background news area 
class BGNews(CreateView, SuccessMessageMixin):
    model = BackgroundImageForNews
    fields = '__all__'
    template_name = 'users/adminpanel/form/bg/new.htm'
    success_url = reverse_lazy('users:postlist')
    success_message = 'Fon yangilandi'

# background main
class BGMain(CreateView, SuccessMessageMixin):
    model = BackgroundImage
    fields = '__all__'
    template_name = 'users/adminpanel/form/bg/new.htm'
    success_url = reverse_lazy('users:postlist')
    success_message = 'Fon yangilandi'

# foto arxiv
def MultiplePhotos(request):
    if request.method == 'POST':
        files = request.FILES.getlist('photos')
        for ph in files:
            photo = PhotoArxiv.objects.create(photos=ph)
            photo.save()
    return render(request, 'users/adminpanel/form/bg/multi_fotos.htm')