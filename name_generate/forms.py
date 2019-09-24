from django import forms
from .models import *


class PersonForm(forms.ModelForm):
    class Meta:
        model = FileName
        fields = ('name', 'birthdate', 'country', 'city')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-country'}),
            'country': forms.Select(attrs={'class': 'form-country', 'style': 'width:100px;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
