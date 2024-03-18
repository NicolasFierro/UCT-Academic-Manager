from django import forms 
from django.core import validators

class FormArticulo(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Titulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ]{5,}$', 'El título está mal digitado', 'invalid_title'),

        ]
    )
    content = forms.CharField(
        label="Contenido",
        max_length=40,
        required=False,
        widget= forms.Textarea(
            attrs= {
                'placeholder': 'Ingrese el Contenido',
                'class':'contenido_form_article'
            }
        )
    )

    public_options= [(0,'No'),(1,'Si')]
    public=forms.TypedChoiceField(
        label='¿publicado?',
        choices=public_options)