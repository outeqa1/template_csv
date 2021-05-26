from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    phone = forms.CharField(label="Phone number",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': '77771234567'}))

    description = forms.CharField(label="Description",
                                  widget=forms.TextInput(
                                         attrs={'class': 'form-control',
                                                'placeholder': 'description'}))

    class Meta:
        model = Record
        fields = ('phone', 'description', 'status')

FIELDS_CHOICES = (
    ('phone', 'phone'),
    ('description', 'description'),
    ('status', 'status'),
    ('created_at', 'created_at')
)

NAME_CHOICES = (
    ('id', 'id'),
    ('username', 'username'),
)

class TemplateForm(forms.Form):
    record_fields = forms.MultipleChoiceField(choices=FIELDS_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)
    name_fields = forms.MultipleChoiceField(choices=NAME_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)