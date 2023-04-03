from django import forms
from .models import AccountBook

class AccountBookForm(forms.ModelForm):
    class Meta:
        model = AccountBook
        fields = ('note', 'description', 'category', 'amount', 'date',)