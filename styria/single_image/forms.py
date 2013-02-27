from django import forms

from models import Image, Rating, Comment


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating