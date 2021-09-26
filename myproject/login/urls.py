from django.urls import include, path
from login import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('api/v1/emp_info/', views.EmpInfo.as_view(), name='emp_info'),
    path('api/v1/all/emps/', views.GetAllEmps.as_view(), name='all_emps'),
    path('api/v1/emp/payroll/', views.EmpPayrollInfo.as_view(), name='emp_payroll'),
    path('api/v1/emp/leave/update/<int:emp_id>/', views.EmpViewAndUpdations.as_view(), name='update_leave'),
    path('api/v1/emp/register/', views.EmpRegistration.as_view(), name='register_emp'),
]