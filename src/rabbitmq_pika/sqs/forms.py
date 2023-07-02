from .models import Default
from django.forms import ModelForm, TextInput


class DefaultForm(ModelForm):
    class Meta:
        model = Default
        fields = [
            'first_number',
            'second_number',
        ]

        widgets = {
            'first_number': TextInput(attrs={
                "class": "form-control"
            }),
            'second_number': TextInput(attrs={
                "class": "form-control"
            }),
        }
