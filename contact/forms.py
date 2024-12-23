from django import forms
from contact.models import Contact

from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Escreva seu primeiro nome',
            }
        ),
        help_text='Nome do contato',
    )

    class Meta:
        model = Contact
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone',
                  'description',
                  'category',
                  'picture',)
 

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'admin':
            raise ValidationError('Invalid first name')
        return first_name