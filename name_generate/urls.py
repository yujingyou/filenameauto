from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.NameGenerateView.as_view(), name='NameGenerate'),
]