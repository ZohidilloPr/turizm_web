from django import forms
from main.models import (
    Post, Hududlar, News, BackgroundImageForAreas, HeaderSlider
)
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewPost(forms.ModelForm):
    uz_post = forms.CharField(widget=CKEditorUploadingWidget())
    ru_post = forms.CharField(widget=CKEditorUploadingWidget())
    en_post = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class NewArea(forms.ModelForm):
    uz_post = forms.CharField(widget=CKEditorUploadingWidget())
    ru_post = forms.CharField(widget=CKEditorUploadingWidget())
    en_post = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Hududlar
        fields = '__all__'

class NewNews(forms.ModelForm):
    uz_post = forms.CharField(widget=CKEditorUploadingWidget())
    ru_post = forms.CharField(widget=CKEditorUploadingWidget())
    en_post = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewHeaderSlider(forms.ModelForm):
    uz_post = forms.CharField(widget=CKEditorUploadingWidget())
    ru_post = forms.CharField(widget=CKEditorUploadingWidget())
    en_post = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = HeaderSlider
        fields = '__all__'

class BGAreas(forms.ModelForm):
    class Meta:
        model = BackgroundImageForAreas
        fields = '__all__'
