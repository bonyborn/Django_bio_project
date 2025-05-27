from django import forms
from .models import Bio

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ['full_name', 'age', 'profession', 'short_bio', 'hobbies']
        widgets = {
            'short_bio': forms.Textarea(attrs={'rows': 4}),
            'hobbies': forms.Textarea(attrs={'rows': 2}),
        }
        labels = {
            'full_name': 'Full Name',
            'age': 'Age',
            'profession': 'Profession',
            'short_bio': 'Short Bio',
            'hobbies': 'Hobbies',
        }