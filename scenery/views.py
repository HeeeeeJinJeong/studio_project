from django.shortcuts import render

# Create your views here.
from .models import Scenery, SceneryCategory

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class SceneryList(ListView):
    model = Scenery
    template_name = 'scenery/scenery_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # pk = 1 : Home
        categories = SceneryCategory.objects.filter(parent_category=SceneryCategory.objects.get(pk=1)).order_by('name')
        kwargs.update({'categories': categories})
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'slug' in self.kwargs:
            try:
                room_category = SceneryCategory.objects.get(slug=self.kwargs['slug'])
                queryset = queryset.filter(category=room_category)
            except:
                pass
        return queryset

class SceneryDetail(DetailView):
    model = Scenery
    template_name = 'scenery/scenery_detail.html'