from django.shortcuts import render

# Create your views here.
from .models import CostumeProduct, CostumeCategory

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class CostumeProductList(ListView):
    model = CostumeProduct
    template_name = 'costume/costume_list.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['categories'] = CostumeCategory.objects.filter(parent_category=CostumeCategory.objects.get(pk=1)).order_by('name')
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'slug' in self.kwargs:
            try:
                category = CostumeCategory.objects.get(slug=self.kwargs['slug'])
                queryset = queryset.filter(category=category)
            except:
                pass
        return queryset


class CostumeProductDetail(DetailView):
    model = CostumeProduct
    template_name = 'costume/costume_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['categories'] = CostumeCategory.objects.filter(parent_category=CostumeCategory.objects.get(pk=1)).order_by('name')
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'slug' in self.kwargs:
            try:
                category = CostumeCategory.objects.get(slug=self.kwargs['slug'])
                queryset = queryset.filter(category=category)
            except:
                pass
        return queryset