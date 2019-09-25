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
        fields = ('project', 'scheme', 'module', 'name', 'date', 'author')
        widgets = {
            'project': forms.Select(),
            'scheme': forms.Select(),
            'module': forms.Select(),
            'name': forms.TextInput(attrs={'value': '请输入文件名称'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'author': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        pkProjectClass = int(kwargs.pop('ProjectClass'))
        print(pkProjectClass)
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(projectclass_id=pkProjectClass).order_by('name')
