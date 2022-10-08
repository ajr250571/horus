from django.shortcuts import render
from core.erp.models import Category
from django.views.generic import ListView


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list_category.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list_category.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Categorias'
        return context
