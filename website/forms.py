from django import forms
from models.models import Articles


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ['title','summary','shortdesc','content', 'sid','status','author']

