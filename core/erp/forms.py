from django import forms
from django.forms import TextInput, Textarea
from core.erp.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingrese el Nombre',
                       'autocomplete': 'off', }
            ),
            'desc': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingrese la Descripcion',
                       'autocomplete': 'off',
                       'rows': 3,
                       'cols': 1, }
            ),
        }
