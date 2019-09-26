from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.NameGenerateView.as_view(), name='NameGenerate'),
    path('techn/<int:pk>', views.TechnicalListView.as_view(), name='Technical'),
    path('ajax/load_scheme_module', views.load_scheme_module, name='ajax_load_scheme_module'),
    path('ajax/generate_name', views.generate_name, name='ajax_generate_name'),
]