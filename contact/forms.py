from django import forms
from contact.models import Contact

from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva seu primeiro nome',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )
    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['first_name'].widget.attrs.update({'placeholder': 'Escreva seu nome'})
    class Meta:
        model = Contact
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone',
                  'description',
                  'category',
                  'picture',)
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'placeholder': 'Escreva seu nome'}),
        # }
    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error('first_name',ValidationError('This is a test error',code='invalid'))

        return super().clean()