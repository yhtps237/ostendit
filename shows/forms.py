from django import forms
from .models import Shows


class ShowsModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    slug = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    published = forms.DateTimeField(label='')

    class Meta:
        model = Shows
        fields = [
            'title',
            'slug',
            'content',
            'published',
            'image',
            'animation'
        ]
