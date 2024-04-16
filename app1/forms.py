from django import forms
from .models import Expense, Tag

from .models import Expense, Tag  # Replace `.models` with your actual model path


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'cost', 'date', 'tags']


    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()  # Dynamically populate tag choices
        # Set an initial value for the tag field (optional)
        self.fields['tags'].initial = Tag.objects.first()  # Select the first tag by default
    tags = forms.ModelChoiceField(queryset=Tag.objects.all(), empty_label="Select Tag", to_field_name="name")
    
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
