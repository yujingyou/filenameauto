from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from name_generate.models import ProjectClass, FlieClass


class NameGenerateView(TemplateView):
    template_name = 'name_generate/base_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech'] = FlieClass.objects.get(name='技术类文件').projectclass_set.all()
        return context


class TechnicalListView(NameGenerateView):
    template_name = 'name_generate/CA.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
