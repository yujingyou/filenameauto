from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.NameGenerateView.as_view(), name='NameGenerate'),
    path('techn/<int:pk>', views.TechnicalListView.as_view(), name='Technical'),
]