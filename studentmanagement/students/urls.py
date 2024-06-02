from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginAsFaculty, name='loginFaculty'),
    path('facultydashboard', views.facultydashboard, name='facultydashboard'),
    path('export/to/excel', views.export_to_excel, name='export_to_excel'),
    path('export/to/word', views.export_to_word, name='export_to_word'),
    path('export/to/xml', views.export_to_xml, name='export_to_xml'),
]
