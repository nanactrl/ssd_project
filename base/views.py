from .models import Task, AuditLog  # ← Added AuditLog here
# This is the method that will be used to log in the user
from django.contrib.auth import login
# This is the form that will be used to create a new user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponseForbidden  # ← Added for admin-only check
# ← NEW: Import for MFA hook (optional; requires django-otp installed)
#from django_otp import devices_for_user


# LoginView in top because it is a gatekeeper for users to access the app


class HomeView(TemplateView):
    template_name = 'base/home.html'


class EnhancedLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True  # Redirects user to tasks page if already logged in

    def get_success_url(self):
        return reverse_lazy('tasks')  # Redirects user to tasks page after successful login

    # ← NEW: Override form_valid for session security and MFA hook
    def form_valid(self, form):
        # Get authenticated user
        user = form.get_user()
        # Regenerate session to prevent fixation attacks (clears old data, creates new ID)
        self.request.session.flush()
        # Optional MFA check: If no device set up, redirect to setup (uncomment to enable)
        # if not devices_for_user(user):
        #     return redirect('mfa_setup')  # Define this URL/view separately if enabling
        # Log in the user
        login(self.request, user)
        return super().form_valid(form)


class RegisterUserPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True  # Redirects user to tasks page if already logged in
    success_url = reverse_lazy('tasks')  # Redirects user to tasks page after successful registration

    def form_valid(self, form):
        user = form.save()  # Saves the user to the database
        if user is not None:
            # ← NEW: Regenerate session to prevent fixation attacks
            self.request.session.flush()
            login(self.request, user)  # Logs in the user after successful registration
        return super(RegisterUserPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterUserPage, self).get(*args, **kwargs)


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'todo_tasks'

    # this method is used to filter the tasks based on the specific user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_tasks'] = context['todo_tasks'].filter(user=self.request.user)
        context['count'] = context['todo_tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'todo_task'
    template_name = 'base/single_task.html'


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']  # Fields that the user can fill out
    success_url = reverse_lazy('tasks')

    # this method is used to assign the user to the task
    def form_valid(self, form):
        form.instance.user = self.request.user  # is the user that is currently logged in
        return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']  # Fields that the user can update
    success_url = reverse_lazy('tasks')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'todo_tasks'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_confirm_delete.html'


# ========================
# USER PROFILE PAGE VIEW
# ========================
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'base/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.request.user
        
        # Optional: Show count of incomplete tasks on profile
        context['incomplete_tasks_count'] = Task.objects.filter(
            user=self.request.user,
            complete=False
        ).count()
        
        return context


# ========================
# AUDIT LOG VIEW (ADMIN ONLY)
# ========================
class AuditLogView(LoginRequiredMixin, TemplateView):
    template_name = 'base/audit_log.html'

    def dispatch(self, request, *args, **kwargs):
        # Only allow users in 'Admin' group
        if not request.user.groups.filter(name='Admin').exists():
            return HttpResponseForbidden(
                "You do not have permission to access the audit log."
            )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Show latest 100 logs (newest first)
        context['logs'] = AuditLog.objects.all()[:100]
        return context