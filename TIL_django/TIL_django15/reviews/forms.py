from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='리뷰 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력',
                'class': 'form-control'}
        ),
    required=True
    )
    

    content = forms.CharField(
        label='리뷰 내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용 입력',
                'class': 'my-content form-control'}
        ),
        required=True
    )

    movie = forms.CharField(
        label='영화 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력',
                'class': 'form-control'}
        ),
    required=True
    )

    class Meta:
        model = Review
        fields = '__all__'

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = '댓글 입력',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용 입력',
                'class': 'my-content form-control'}
        ),
    )

    class Meta:
        model = Comment
        fields = ('content',)