from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['pair','session','pips','date', 'entry_time','comment', 'before_chart','after_chart']
        widgets = {
            'pair': forms.TextInput(attrs={'class' : 'form-control'}),
            'session': forms.TextInput(attrs={'class' : 'form-control'}),
            'pips': forms.TextInput(attrs={'class' : 'form-control'}),
            'date': forms.DateInput(attrs={'class' : 'form-control'}),
            'entry_time': forms.TextInput(attrs={'class' : 'form-control'}),
            'comment': forms.TextInput(attrs={'class' : 'form-control'}),
            'before_chart': forms.TextInput(attrs={'class' : 'form-control'}),
            'after_chart': forms.TextInput(attrs={'class' : 'form-control'}),

        }