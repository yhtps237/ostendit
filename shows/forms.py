from django import forms
from .models import Shows


class ShowsModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    slug = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Your title but lowercase and replace spaces with "-". ', 'class': 'form-control'}))
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    # published = forms.DateTimeField(
    #     label='', widget=forms.DateInput(attrs={'placeholder': 'asdf'}))
    published = forms.DateTimeField(
        widget=forms.DateInput(attrs={'placeholder': 'yy-mm-dd   hh-mm-ss'}))

    class Meta:
        model = Shows
        fields = [
            'title',
            'slug',
            'content',
            'published',
            'image',
            'animation',
        ]
