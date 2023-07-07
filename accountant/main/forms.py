from django import forms
from .models import ParserConfig

class ParserConfigRadioSelect(forms.ModelForm):
    class Meta:
        model = ParserConfig
        fields = '__all__'
        widgets = {
            'flag': forms.RadioSelect,
        }
