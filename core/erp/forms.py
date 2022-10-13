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
                       'rows': 4,
                       'cols': 1, }
            ),
        }
    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data
