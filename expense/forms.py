from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    """docstring for ."""

    class Meta:
        model= Expense
        fields = "__all__"
        labels={
            'description': 'Name Expense'

        }
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select'
        self.fields['payment'].empty_label = ' Select'
