from django import forms
from .models import ParserConfig, ParserResult

class ParserConfigRadioSelect(forms.ModelForm):
    class Meta:
        model = ParserConfig
        fields = '__all__'
        widgets = {
            'flag': forms.RadioSelect,
        }

class ParserResultRadioSelect(forms.ModelForm):
    class Meta:
        model = ParserResult
        fields = '__all__'
        widgets = {
            'flag': forms.RadioSelect,
        }