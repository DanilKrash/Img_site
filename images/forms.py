from django import forms

from images.models import Comment, Img


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ('title', 'img')
