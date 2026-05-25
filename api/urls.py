# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_index, name='welcome-index'),

    # Task API Endpoints
    path('tasks', views.create_task, name='create-task'),
    path('employees', views.register_employee, name='register-employee'),
    path('assign', views.assign_task, name='assign-task'),
    path('employees/<int:id>/tasks', views.employee_tasks, name='employee-tasks'),
]
