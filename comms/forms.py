from django import forms
from .models import Article

class CreateUserArticleForm(forms.ModelForm):
    text = forms.CharField(
        max_length=140,
        help_text='140字以内で入力してください。'
    )
    class Meta():
        model = Article
        fields = ('text', )