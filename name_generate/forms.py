from django import forms
from .models import *


class BaseForm(forms.ModelForm):
    class Meta:
        model = TechniFileName

        fields = ('project', 'scheme', 'module', 'name', 'date', 'author')
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TechnicalForm(forms.ModelForm):
    class Meta:
        model = TechniFileName
        fields = ('project', 'scheme', 'module', 'name', 'date', 'author', 'version', 'number', 'result')

        widgets = {
            'project': forms.Select(),
            'scheme': forms.Select(),
            'module': forms.Select(),
            'name': forms.TextInput(attrs={'placeholder': '请输入文件名称', 'value': ''}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'author': forms.TextInput(),
            'version': forms.TextInput(attrs={'style': "display:none;"}),
            'number': forms.TextInput(attrs={'style': "display:none;"}),
            'result': forms.TextInput(attrs={'style': "border:none;cursor:text", 'readonly': 'true'}),
        }

    def __init__(self, *args, **kwargs):
        pkProjectClass = int(kwargs.pop('ProjectClass'))
        print(pkProjectClass)
        super().__init__(*args, **kwargs)
        self.fields['scheme'].queryset = Scheme.objects.none()
        self.fields['module'].queryset = Module.objects.none()
        self.fields['project'].queryset = Project.objects.filter(projectclass_id=pkProjectClass).order_by('name')

        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['scheme'].queryset = Scheme.objects.filter(project_id=project_id).order_by('name')
                self.fields['module'].queryset = Module.objects.filter(project_id=project_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['scheme'].queryset = self.instance.project.scheme_set.order_by('name')
            self.fields['module'].queryset = self.instance.project.module_set.order_by('name')


class PlanForm(forms.ModelForm):
    class Meta:
        model = PlanFileName
        fields = ('project', 'phase', 'date', 'name', 'author','number','result')
        widgets = {
            'project': forms.Select(),
            'phase': forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'placeholder': '请输入文件名称', 'value': ''}),
            'author': forms.TextInput(),
            'number': forms.TextInput(attrs={'style': "display:none;"}),
            'result': forms.TextInput(attrs={'style': "border:none;cursor:text", 'readonly': 'true'}),
        }

    def __init__(self, *args, **kwargs):
        pkProjectClass = int(kwargs.pop('ProjectClass'))
        print(pkProjectClass)
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(projectclass_id=pkProjectClass).order_by('name')


class RecordForm(forms.ModelForm):
    class Meta:
        model = RecordFileName
        fields = ('project', 'date', 'name', 'author','number','result')
        widgets = {
            'project': forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'placeholder': '请输入文件名称', 'value': ''}),
            'author': forms.TextInput(),
            'number': forms.TextInput(attrs={'style': "display:none;"}),
            'result': forms.TextInput(attrs={'style': "border:none;cursor:text", 'readonly': 'true'}),
        }

    def __init__(self, *args, **kwargs):
        pkProjectClass = int(kwargs.pop('ProjectClass'))
        print(pkProjectClass)
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(projectclass_id=pkProjectClass).order_by('name')
