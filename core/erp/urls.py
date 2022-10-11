from django.contrib import admin
from django.urls import path
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path("category/list/", CategoryListView.as_view(), name="category_list"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path("category/update/<int:pk>/", CategoryUpdateView.as_view(), name="category_update"),
]
