from django import forms
from .models import Expense, Tag

from .models import Expense, Tag  # Replace `.models` with your actual model path


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'cost', 'date', 'tags']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


   
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
