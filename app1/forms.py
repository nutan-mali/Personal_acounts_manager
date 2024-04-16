from django import forms
from .models import Expense, Tag

from .models import Expense, Tag  # Replace `.models` with your actual model path


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'cost', 'date', 'tags']


   
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
