from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import Post

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'challenge_type', 'description', 'link', 'date', 'poster']
        widgets = {
            'date': DatePickerInput()
        }
