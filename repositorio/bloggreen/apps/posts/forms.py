from django import forms
from apps.posts.models import Post, Comment
from django.conf import settings

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            'title',
            'content',
            'thumbnail',
            'categoria',
        ]

        labels = {
            'title': 'Ingrese el titulo'
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            'title',
            'content',
            'thumbnail',
            'categoria',
        ]

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment

		fields = [
			'content',
		]