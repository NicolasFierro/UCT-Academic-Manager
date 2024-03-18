from django import forms

class FormArticulo(forms.Form):
    title= forms.CharField(label="Titulo")

    content= forms.forms.CharField(label="Contenido",widget= forms.Textarea)

    title= forms.BooleanField(label="Public")

    public_option = [(0,'No'),(1,'Si')]
    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_option
    )