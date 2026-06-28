from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_list, name='lead_list'),

    path(
        'export/csv/',
        views.export_csv,
        name='export_csv'
    ),

    path(
        'export/excel/',
        views.export_excel,
        name='export_excel'
    ),
]