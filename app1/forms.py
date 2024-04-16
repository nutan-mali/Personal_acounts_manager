from django import forms
from .models import Expense, Tag

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'cost', 'date', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
