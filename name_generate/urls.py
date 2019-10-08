from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.NameGenerateView.as_view(), name='NameGenerate'),
    path('techn/<int:pk>', views.TechnicalListView.as_view(), name='Technical'),
    path('plan/<int:pk>', views.PlanListView.as_view(), name='Plan'),
    path('record/<int:pk>', views.RecordListView.as_view(), name='Record'),
    path('ajax/load_scheme_module', views.load_scheme_module, name='ajax_load_scheme_module'),
    path('ajax/ajax_generate_tfname', views.generate_technical_file_name, name='ajax_generate_tfname'),
    path('ajax/ajax_generate_pfname', views.generate_plan_file_name, name='ajax_generate_pfname'),
    path('ajax/ajax_generate_rfname', views.generate_record_file_name, name='ajax_generate_rfname'),
]
