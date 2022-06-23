from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, TimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','announcement', 'full_text', 'date', 'time']

        widgets = {
            'title' : TextInput(attrs= {
                'class':'form-control',
                'placeholder':'Название статьи'
            }),
            'announcement': TextInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'full_text': Textarea(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'date': DateTimeInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'time': TimeInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Время публикации'
            })
        }
