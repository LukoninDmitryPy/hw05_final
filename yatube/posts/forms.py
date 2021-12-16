from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image',)
        help_texts = {
            'text': 'Запиши свои мысли',
            'group': 'Выбери приближенную группу из списка',
        }
        labels = {
            'text': 'Текст поста',
            'group': 'Группа поста',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        help_texts = {
            'text': 'Запиши свои мысли',
        }
        labels = {
            'text': 'Текст комментарии',
        }