import logging

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task, AuditLog

# -------------------------------------------------------------------
# Logger configuration (OWASP ASVS V3 – Safe Logging)
# -------------------------------------------------------------------
logger = logging.getLogger(__name__)


# ========================
# HOME VIEW
# ========================
class HomeView(TemplateView):
    template_name = 'base/home.html'


# ========================
# LOGIN VIEW (SECURE)
# ========================
class EnhancedLoginView(LoginView):
    template_name = 'base/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.get_user()

        # ✅ SAFE LOGGING (NO PASSWORDS / TOKENS)
        logger.info(
            "User login successful",
            extra={"username": user.username}
        )

        # Optional: Store audit trail (no sensitive data)
        AuditLog.objects.create(
            user=user,
            action="LOGIN_SUCCESS"
        )

        # Prevent session fixation
        self.request.session.flush()

        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        username = form.data.get("username")

        # ✅ SAFE FAILED LOGIN LOG
        logger.warning(
            "User login failed",
            extra={"username": username}
        )

        AuditLog.objects.create(
            user=None,
            action=f"LOGIN_FAILED ({username})"
        )

        return super().form_invalid(form)


# ========================
# REGISTRATION VIEW
# ========================
class RegisterUserPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            logger.info(
                "New user registered",
                extra={"username": user.username}
            )

            AuditLog.objects.create(
                user=user,
                action="USER_REGISTERED"
            )

            # Prevent session fixation
            self.request.session.flush()
            login(self.request, user)

        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(*args, **kwargs)


# ========================
# TASK LIST VIEW
# ========================
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'todo_tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_tasks'] = context['todo_tasks'].filter(
            user=self.request.user
        )
        context['count'] = context['todo_tasks'].filter(
            complete=False
        ).count()
        return context


# ========================
# TASK DETAIL VIEW
# ========================
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'todo_task'
    template_name = 'base/single_task.html'


# ========================
# CREATE TASK
# ========================
class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# ========================
# UPDATE TASK
# ========================
class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


# ========================
# DELETE TASK
# ========================
class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'todo_tasks'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_confirm_delete.html'


# ========================
# USER PROFILE
# ========================
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'base/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.request.user
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
        if not request.user.groups.filter(name='Admin').exists():
            return HttpResponseForbidden(
                "You do not have permission to access the audit log."
            )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logs'] = AuditLog.objects.all().order_by('-id')[:100]
        return context
