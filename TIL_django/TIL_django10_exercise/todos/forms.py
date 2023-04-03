from django import forms
from .models import Todo
from .validators import *
import re

class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력',
                'class': 'form-control'}
    ),
    validators=[first_validator],
    required=True
    )
    

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용 입력',
                'class': 'my-content form-control'}
        ),
        required=True
    )
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content:
            content = re.sub(r'[a-zA-z]+', '', content) #영어제거.. 애초에 경고하는 법은 어떻게 할까?
        return content

    
    priority = forms.IntegerField(
        label='우선 순위',
        widget=forms.NumberInput(
            attrs={
                'min': 1, 'max': 5, 'value': 3,
                'class': 'form-control'}
        ),
        required=True
    )

    deadline = forms.DateField(
        label='마감 기한',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'}
        ),
        required=True
    )
    class Meta:
        model = Todo
        exclude = ('completed',)