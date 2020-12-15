from task.views import login, tenant_view, add_employee, add_task, provide_task, emp_view,logout
from django.urls import path

urlpatterns = [
    path('', emp_view),
    path('logout',logout),
    path('login', login),
    path('tenant', tenant_view),
    path('add_employee', add_employee),
    path('add_task', add_task),
    path('assign_task/', provide_task, name='assign_url'),
]
