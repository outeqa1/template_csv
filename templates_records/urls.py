from django.urls import path
from .views import home, template, RecordDetailView, RecordCreateView

urlpatterns = [
    path('', home, name="home"),
    path('record/<int:pk>/', RecordDetailView.as_view(), name="record"),
    path('add/', RecordCreateView.as_view(), name='add'),
    path('template/', template, name='template'),
]