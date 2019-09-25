from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from name_generate.forms import BaseForm, TechnicalForm
from name_generate.models import ProjectClass, FlieClass, TechniFileName, Scheme, Module


class NameGenerateView(CreateView):
    model = FlieClass
    form_class = BaseForm
    template_name = 'name_generate/base_view.html'
    success_url = reverse_lazy('NameGenerate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech'] = FlieClass.objects.get(name='技术类文件').projectclass_set.all()
        return context


class TechnicalListView(NameGenerateView):
    template_name = 'name_generate/CA.html'
    form_class = TechnicalForm
    success_url = reverse_lazy('NameGenerate')
    model = ProjectClass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projectclass'] = ProjectClass.objects.get(pk=self.get_pk())
        return context

    def get_pk(self):
        path = str(self.request.path)
        pos = path.rfind('/')
        if pos != -1:
            return path[pos + 1:]
        else:
            raise Exception('get_pk 不是正确的路径,获取不到数据库对象')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs.update({
            'ProjectClass': self.get_pk()
        })
        return kwargs


def load_scheme_module(request):
    project_id = request.GET.get('project')
    schemes = Scheme.objects.filter(project_id=project_id).order_by('name')
    modules = Module.objects.filter(project_id=project_id).order_by('name')
    return render(request, 'name_generate/scheme_module_list_option.html', {'schemes': schemes, 'modules': modules})
