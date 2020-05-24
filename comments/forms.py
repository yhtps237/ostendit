from django import forms
from .models import Comment


class CommentModelForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = [
            'comment'
        ]
