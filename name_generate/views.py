from django.shortcuts import render, HttpResponse
import json
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from name_generate.forms import BaseForm, TechnicalForm, PlanForm, RecordForm
from name_generate.models import ProjectClass, FlieClass, TechniFileName, Scheme, Module
from name_generate.FileNameAuto import TechnicalFileNameAuto, PlanFileNameAuto, RecordFileNameAuto


class NameGenerateView(CreateView):
    model = FlieClass  # 关联的数据表
    form_class = BaseForm  # 关联的表单类
    template_name = 'name_generate/base_view.html'  # 模板路径
    success_url = reverse_lazy('NameGenerate')  # 表单提交后跳转url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech'] = FlieClass.objects.get(name='技术类文件').projectclass_set.all()
        context['plan'] = FlieClass.objects.get(name='计划类文件').projectclass_set.all()
        context['record'] = FlieClass.objects.get(name='记录类文件').projectclass_set.all()
        return context


class TechnicalListView(NameGenerateView):
    template_name = 'name_generate/Technical.html'
    form_class = TechnicalForm

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


class PlanListView(NameGenerateView):
    template_name = 'name_generate/plan.html'
    form_class = PlanForm

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


class RecordListView(NameGenerateView):
    template_name = 'name_generate/Record.html'
    form_class = RecordForm

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


def generate_technical_file_name(request):
    if request.method == "POST" and request.POST:
        validData = TechnicalForm(request.POST)
        if validData.is_valid():
            print("is_valid")
        else:
            print(validData.errors)

    technicalFileName = TechnicalFileNameAuto(project=request.GET.get('project'),
                                              scheme=request.GET.get('scheme'),
                                              module=request.GET.get('module'),
                                              name=request.GET.get('name'),
                                              date=request.GET.get('date'),
                                              author=request.GET.get('author'),
                                              version=request.GET.get('version'))
    result = technicalFileName.getFileName()
    data = [{'number': technicalFileName.number, 'version': technicalFileName.version, 'result': result}]
    ret = json.dumps(data)
    return HttpResponse(ret)


def generate_plan_file_name(request):
    if request.method == "POST" and request.POST:
        validData = PlanForm(request.POST)
        if validData.is_valid():
            print("is_valid")
        else:
            print(validData.errors)

    planFileName = PlanFileNameAuto(project=request.GET.get('project'),
                                    phase=request.GET.get('phase'),
                                    name=request.GET.get('name'),
                                    date=request.GET.get('date'),
                                    author=request.GET.get('author'),
                                    )
    result = planFileName.getFileName()
    data = [{'number': planFileName.number, 'result': result}]
    ret = json.dumps(data)
    return HttpResponse(ret)


def generate_record_file_name(request):
    if request.method == "POST" and request.POST:
        validData = RecordForm(request.POST)
        if validData.is_valid():
            print("is_valid")
        else:
            print(validData.errors)

    planFileName = RecordFileNameAuto(project=request.GET.get('project'),
                                      name=request.GET.get('name'),
                                      date=request.GET.get('date'),
                                      author=request.GET.get('author'),
                                      )
    result = planFileName.getFileName()
    data = [{'number': planFileName.number, 'result': result}]
    ret = json.dumps(data)
    return HttpResponse(ret)
