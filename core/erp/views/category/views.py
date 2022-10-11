from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from core.erp.forms import CategoryForm
from core.erp.models import Category
from django.views.generic import ListView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list_category.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list_category.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name': 'Willian'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Categorias'
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create_category.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación de Categorias'
        return context
