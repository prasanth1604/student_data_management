from django.urls import path
from . import views

urlpatterns = [
    # path('', include('home.urls')),
    # path('', views.login, name='login'),
    path('', views.loginAsFaculty, name='loginFaculty'),
    # path('stdashboard', views.dashboard, name='dashboard'),
    path('facultydashboard', views.facultydashboard, name='facultydashboard'),
    path('export/students/', views.export_students_to_excel, name='export_students_to_excel'),
]
