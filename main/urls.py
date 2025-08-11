from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.dashboard, name='dashboard_page'),
    path('login/', views.login_view, name='login'),
    path('compliance-actions/', views.compliance_actions, name='compliance_actions'),
    path('compliance-management/', views.compliance_management, name='compliance_management'),
    path('compliance-creation/', views.compliance_creation, name='compliance_creation'),
    path('admin-compliance-creation/', views.admin_compliance_creation, name='admin_compliance_creation'),
    path('compliance-edit-delete/', views.compliance_edit_delete, name='compliance_edit_delete'),
    path('create-user/', views.create_user, name='create_user'),
    path('edit-credentials/', views.edit_credentials, name='edit_credentials'),
    path('password-change/', views.password_change, name='password_change'),
    path('edit-compliance/', views.edit_compliance, name='edit_compliance'),
    path('user-landing/', views.user_landing, name='user_landing'),
    path('compliance-details/<str:selected_date>/', views.compliance_details, name='compliance_details'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard_page'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
] 