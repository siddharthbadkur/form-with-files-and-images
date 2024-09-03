from .models import *
from  django import forms

class InfoItem(forms.ModelForm):
    class Meta:
        model = resume
        fields='__all__'