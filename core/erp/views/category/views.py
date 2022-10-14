from webbrowser import get
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from core.erp.forms import CategoryForm
from core.erp.models import Category
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list_category.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Categorias'
        context["create_url"] = reverse_lazy('erp:category_create')
        context["list_url"] = reverse_lazy('erp:category_list')
        context["entity"] = 'Categorias'
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create_category.html'
    success_url = reverse_lazy('erp:category_list')

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    #     print(request.POST)
    #     form = CategoryForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación de Categorias'
        context["list_url"] = reverse_lazy('erp:category_list')
        context["entity"] = 'Categorias'
        # context["action"] = 'add'
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/update_category.html"
    success_url = reverse_lazy('erp:category_list')

    # def post(self, request, *args, **kwargs ):


    def get_context_data(self, **kwargs):
        # print(self.object)
        # print(self.get_object())
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edicion de Categoria'
        context["list_url"] = reverse_lazy('erp:category_list')
        context["entity"] = 'Categorias'
        # context["action"] = 'edit'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/delete_category.html"
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminación de Categoria'
        context["list_url"] = reverse_lazy('erp:category_list')
        context["entity"] = 'Categorias'
        # context["action"] = 'delete'
        return context
