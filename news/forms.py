from django import forms
from .models import News
from django.core.exceptions import ValidationError

class NewsForms(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'author',
            'created_at',
        ]
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'})
        }

        def clean(self):
            cleaned_data = super().clean()
            content = cleaned_data.get("cleaned_data ")
            if content is not None and len(content)<20:
                raise ValidationError({
                    "content: Содержание не может быть меньше 20 символов"
                })
            return cleaned_data

