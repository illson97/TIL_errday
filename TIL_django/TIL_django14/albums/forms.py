from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력칸',
                'class': 'form-control'
            }
        ),
        required=True
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용 입력',
                'class': 'my-content form-control'
            }
        ),
        required=True
    )
   
    class Meta:
        model = Album
        fields = '__all__'
