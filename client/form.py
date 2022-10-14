from django import  forms
from .models import Raqam


class RaqamForms(forms.ModelForm):
    class Meta:
        model = Raqam
        fields = "__all__"
