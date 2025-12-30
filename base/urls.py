from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (
    TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask,
    EnhancedLoginView, RegisterUserPage, HomeView,
    ProfileView, AuditLogView  
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', EnhancedLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # ← Works perfectly
    path('register/', RegisterUserPage.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
    path('audit-log/', AuditLogView.as_view(), name='audit_log'),  # ← FINAL MISSING URL

]