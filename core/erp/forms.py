from django import forms
from django.forms import TextInput, Textarea
from core.erp.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={'placeholder': 'Ingrese el Nombre',
                       'autofocus': True, }
            ),
            'desc': Textarea(
                attrs={'placeholder': 'Ingrese la Descripcion',
                       'rows': 3,
                       'cols': 1, }
            ),
        }
