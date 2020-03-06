from django import forms
from django.forms import modelformset_factory
from .models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'text': 'Question'
        }
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Question ...',
            }
            )
        }


AnswerFormSet = modelformset_factory(
    Answer,
    fields='__all__',
    extra=1,
    widgets={
            'text': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Option'
                }
            )
        }
)
