from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify
from django.contrib.auth.models import User  # Import the User model
from Filmapp.models import Movie, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'trailer_link', 'genre']
        widgets = {
            'release_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from the kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        title = self.cleaned_data.get('title')
        if title and not instance.slug:  # Only generate slug if it doesn't exist
            instance.slug = slugify(title)
        if commit:
            instance.save()
        return instance

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title:
            # Generate slug from the title
            cleaned_data['slug'] = slugify(title)
        return cleaned_data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')