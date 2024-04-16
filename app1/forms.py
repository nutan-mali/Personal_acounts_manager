from django import forms
from .models import Expense, Tag

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
