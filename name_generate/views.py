from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, TemplateView


class NameGenerateView(TemplateView):
    template_name = 'name_generate/base_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = None
        return context
